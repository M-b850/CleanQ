from rest_framework import generics, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.shortcuts import get_list_or_404

from clinic.serializers import ClinicSerializer
from reservation.serializers import ReservationSerializer
from core.models import Clinic, Reservation


class CreateClinicView(generics.CreateAPIView):
    """Create a new clinic"""
    serializer_class = ClinicSerializer


class WatchClinicView(APIView):
    """Watch the clinic user"""
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()
    authentication_classes = (authentication.TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        if request.user.type == 'CLINIC':
            clinic = get_list_or_404(Clinic, user_id=self.request.user.pk)
            serializer = ClinicSerializer(clinic, many=True)
            return Response(serializer.data)
        else:
            raise PermissionDenied(
                {
                    "Message": "You don't have permission to access",
                    "Help": "Create a Clinic account."
                }
            )

class WatchReservedForClinic(generics.ListAPIView):
    """List of reserved for clinic"""
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = (authentication.TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.type == 'CLINIC':
            queryset = self.queryset
            return queryset.filter(clinic__user=self.request.user)
        raise PermissionDenied(
            {
                "Message": "You don't have permission to access",
                "Help": "Create a Clinic account."
            }
        )

    def get(self, request):
        reserves = self.get_queryset()
        serializer = ReservationSerializer(reserves, many=True)
        return Response(serializer.data)
