from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, force_authenticate
from rest_framework import status

from core.models import Clinic, Reservation

from datetime import datetime, timezone


CREATE_RESERVE_URL = reverse('reservation:create')


class PublicReservationApiTests(TestCase):

    def setUp(self):
        # User:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='woh@formaloo.com',
            password='its-latenight',
        )
        self.owner = get_user_model().objects.create_user(
            email='test@testformaloo.com', 
            password='Testcase123',
        )
        self.client.force_authenticate(user=self.user)

        # Clinic:
        self.clinic = Clinic.objects.create(cname='Haj-khanum-kolsom', user=self.owner)

    def test_make_reservation(self):
        '''Test for creating a reservation as a user'''
        payload = {
            'user': f'{self.user.pk}',
            'clinic': f'{self.clinic.pk}',
            'up_date': f'{datetime.now(timezone.utc)}',
        }
        res = self.client.post(CREATE_RESERVE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)