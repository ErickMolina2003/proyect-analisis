"""
Test for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is succesful"""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email, password='sample123', dni=email)
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test creating a user without an eamil reaises a value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'sample123')

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'sample123',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_partner(self):
        """Test creating a partner is successful."""
        partner = models.Partner.objects.create(
            first_name='Partner example',
            dni='12345678',
            is_active=True,
            address='La Canada',
        )
        self.assertEqual(str(partner), partner.first_name)

    def test_create_motorist(self):
        """Test creating a motorist is successful."""
        partner = models.Partner.objects.create(
            first_name='Partner example',
            dni='12345678',
            is_active=True,
            address='La Canada',
        )
        motorist = models.Motorist.objects.create(
            id_partner=partner,
            first_name='Motorist example',
            dni='12345678',
            is_active=True,
            address='La Canada',
        )
        self.assertEqual(str(motorist), motorist.first_name)
        self.assertEqual(partner.id, motorist.id_partner.id)

    def test_create_truck(self):
        """Test creating a truck is successfull"""
        partner = models.Partner.objects.create(
            first_name='Sample Partner',
            dni='12345678',
            address='La Canada',
        )
        truck = models.Truck.objects.create(
            id_partner=partner,
            truck_number='12345',
            is_active=False,
        )
        self.assertEqual(str(truck), truck.truck_number)
        self.assertEqual(truck.id_partner.id, partner.id)

    def test_create_client(self):
        """Test creating a client is successfull"""
        client = models.Client.objects.create(
            first_name='Sample Client',
            last_name='Sample Client last name',
            address='Sample Client address',
            rtn='12345678',
            phone_number='12345687',
            email='example@example.com',
        )
        self.assertEqual(str(client), client.first_name)
