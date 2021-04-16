from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Clinic, Reservation

from clinic import serializers


class ClinicViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    """Manage Database in database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Clinic.objects.all()
    serializer_class = serializers.ClinicSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('name')

    def perform_create(self, serializer):
        """Create a new clinic"""
        serializer.save(user=self.request.user)


class ReservationViewSet(viewsets.ModelViewSet):
    """Manage Reservations in the database"""
    serializer_class = serializers.ReservationSerializer
    queryset = Reservation.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Retrieve for authenticated user"""
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Create a new Reservation"""
        serializer.save(user=self.request.user)
