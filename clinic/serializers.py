from core.models import Clinic, Reservation
from user.serializers import UserSerializer

from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model, authenticate


class ClinicSerializer(serializers.ModelSerializer):
    '''Serializer for clinic object'''
    user = UserSerializer()

    class Meta:
        model = Clinic
        fields = ('cname', 'user',)
        extra_kwargs = {
            'cname': {'help_text': 'Enter clinics name.'},
        }

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = get_user_model().objects.create_user(**user_data)
        user.type = 'CLINIC'
        clinic = Clinic.objects.create(user=user, **validated_data)
        return clinic
