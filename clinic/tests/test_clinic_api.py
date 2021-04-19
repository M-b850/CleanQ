from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, force_authenticate
from rest_framework import status

CREATE_CLINIC_URL = reverse('clinic:create')
CLINIC_URL = reverse('clinic:me')

class PublicClinicApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_clinic(self):
        '''create a clinic without registerd user'''
        payload = {
        'cname': 'Haj Aqa reza',
        'user': {
                'email': 'test@testformaloo.com', 
                'password': 'Testcase123',
                'name': 'Abbas',
                'last_name': 'babaei',
            }
        }
        res = self.client.post(
            CREATE_CLINIC_URL,
            payload,
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn('Haj Aqa reza', res.data['cname'])
