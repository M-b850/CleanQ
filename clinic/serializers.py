from rest_framework import serializers

from core.models import Clinic, Reservation


class ClinicSerializer(serializers.ModelSerializer):
    """Serializer for clinic object"""

    class Meta:
        model = Clinic
        fields = ('id', 'name')
        read_only_fields = ('id',)


class ReservationSerializer(serializers.ModelSerializer):
    """Serialize a reservation"""

    class Meta:
        model = Reservation
        fields = ('id', 'user', 'clinic', 'up_date', 'comment')
        read_only_fields = ('id', 'user')
