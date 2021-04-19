from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Clinic, Reservation
from datetime import datetime, timezone


class ModelTest(TestCase):

    def test_create_clinic(self):
        email = 'ali-gerayli@Formaloo.com'
        password = 'my-password@'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        clinic_name = 'Zakarya Razi'
        clinic = Clinic.objects.create(
            name='Zakarya Razi',
            user=user,
        )
        self.assertEqual(clinic.name, clinic_name)
        self.assertTrue(clinic.user.check_password(password))
        self.assertEqual(clinic.owner_id, user.pk)
        self.assertTrue(clinic.user.email, email)
        self.assertEqual(user.type, 'PATIENT')

    def test_create_reservation(self):
        '''Test crearte a succesful reservation.'''
        user = get_user_model().objects.create_user(
            email='ali-gerayli@Formaloo.com',
            password='my-password@'
        )
        clinic = Clinic.objects.create(
            name='Zakarya Razi',
            user=user,
        )
        reserve = Reservation.objects.create(
            user=user, 
            clinic=clinic,
            up_date=datetime.now(timezone.utc),
        )
        self.assertFalse(reserve.canceled)
        self.assertEqual(reserve.user, user)
        self.assertEqual(reserve.clinic, clinic)
        