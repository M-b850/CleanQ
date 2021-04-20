from rest_framework import generics
from rest_framework import generics, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.shortcuts import get_list_or_404

from reservation.serializers import ReservationSerializer
from clinic.serializers import ClinicSerializer

from core.models import Reservation, Clinic

from datetime import datetime, timezone



class CreateReservationView(generics.CreateAPIView):
    serializer_class = ReservationSerializer
    authentication_classes = (authentication.TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ListReservationView(APIView):
    '''List all reservations'''
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    authentication_classes = (authentication.TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        lt = self.request.query_params.get('lt')
        gte = self.request.query_params.get('rte')
        queryset = self.queryset

        if lt: # Past
            queryset = queryset.filter(up_date__lt=datetime.now(timezone.utc))        
        if gte: # Upcoming 
            queryset = queryset.filter(up_date__gte=datetime.now(timezone.utc))   
        
        return queryset.filter(user=self.request.user)

    def get(self, request, format=None):
        reserv = self.get_queryset()        
        serializer = ReservationSerializer(reserv, many=True)
        return Response(serializer.data)


class ListClinicsView(APIView):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()
    authentication_classes = (authentication.TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        reserv = self.queryset.all()
        serializer = ClinicSerializer(reserv, many=True)
        return Response(serializer.data)