from core.models import Reservation

from rest_framework import serializers


class ReservationSerializer(serializers.ModelSerializer):
    """Serialize Reservation"""
    
    class Meta:
        model = Reservation
        fields = (
            'id',
            'user', 
            'clinic', 
            'created_date',
            'up_date',
            'comment',
        )
        read_only_fields = ('id', 'user', 'created_date')

    def create(self, validated_data):
        reserve = Reservation.objects.create(**validated_data)
        return reserve
