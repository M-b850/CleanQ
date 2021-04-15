from rest_framework import serializers

from core.models import Clinic


class ClinicSerializer(serializers.ModelSerializer):
    """Serializer for clinic object"""

    class Meta:
        model = Clinic
        fields = ('id', 'name')
        read_only_fields = ('id',)
