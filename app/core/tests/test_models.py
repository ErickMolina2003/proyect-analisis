"""
Test for models
"""
from decimal import Decimal

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

    def test_create_freight(self):
        """Test creating a freight is successfull"""
        client = models.Client.objects.create(
            first_name='Sample Client',
            last_name='Sample Client last name',
            address='Sample Client address',
            rtn='12345678',
            phone_number='12345687',
            email='example@example.com',
        )
        partner = models.Partner.objects.create(
            first_name='Sample Partner',
            dni='12345678',
            address='La Canada',
        )
        motorist = models.Motorist.objects.create(
            id_partner=partner,
            first_name='Motorist example',
            dni='12345678',
            is_active=True,
            address='La Canada',
        )
        truck = models.Truck.objects.create(
            id_partner=partner,
            truck_number='12345',
            is_active=False,
        )
        freight = models.Freight.objects.create(
            id_client=client,
            id_partner=partner,
            id_motorist=motorist,
            id_truck=truck,
            supervisor_client='Erick Molina',
            description='Pedido 505 a res canada',
            sub_total=Decimal('1024.30'),
            importe_gravado=Decimal('123.20'),
            isv=Decimal('25.23'),
            total=Decimal('1230.23'),
            is_completed=False,
            payment_method='Efectivo'
        )
        self.assertTrue(str(freight), freight.description)
        self.assertTrue(freight.id_client.id, client.id)
        self.assertTrue(freight.id_partner.id, partner.id)
        self.assertTrue(freight.id_motorist.id, motorist.id)
        self.assertTrue(freight.id_truck.id, truck.id)

    def test_create_billing_successful(self):
        """Test creating a billing"""
        client = models.Client.objects.create(
            first_name='Sample Client',
            last_name='Sample Client last name',
            address='Sample Client address',
            rtn='12345678',
            phone_number='12345687',
            email='example@example.com',
        )
        partner = models.Partner.objects.create(
            first_name='Sample Partner',
            dni='12345678',
            address='La Canada',
        )
        motorist = models.Motorist.objects.create(
            id_partner=partner,
            first_name='Motorist example',
            dni='12345678',
            is_active=True,
            address='La Canada',
        )
        truck = models.Truck.objects.create(
            id_partner=partner,
            truck_number='12345',
            is_active=False,
        )
        freight = models.Freight.objects.create(
            id_client=client,
            id_partner=partner,
            id_motorist=motorist,
            id_truck=truck,
            supervisor_client='Erick Molina',
            description='Pedido 505 a res canada',
            sub_total=Decimal('1024.30'),
            importe_gravado=Decimal('123.20'),
            isv=Decimal('25.23'),
            total=Decimal('1230.23'),
            is_completed=False,
            payment_method='Efectivo'
        )
        billing = models.Billing.objects.create(
            id_freight=freight,
            date='2003-12-12',
        )
        self.assertTrue(billing.id_freight.id, freight.id)

    def test_creating_commission_payment(self):
        """Test creating a commission payment"""
        client = models.Client.objects.create(
            first_name='Sample Client',
            last_name='Sample Client last name',
            address='Sample Client address',
            rtn='12345678',
            phone_number='12345687',
            email='example@example.com',
        )
        partner = models.Partner.objects.create(
            first_name='Sample Partner',
            dni='12345678',
            address='La Canada',
        )
        motorist = models.Motorist.objects.create(
            id_partner=partner,
            first_name='Motorist example',
            dni='12345678',
            is_active=True,
            address='La Canada',
        )
        truck = models.Truck.objects.create(
            id_partner=partner,
            truck_number='12345',
            is_active=False,
        )
        freight = models.Freight.objects.create(
            id_client=client,
            id_partner=partner,
            id_motorist=motorist,
            id_truck=truck,
            supervisor_client='Erick Molina',
            description='Pedido 505 a res canada',
            sub_total=Decimal('1024.30'),
            importe_gravado=Decimal('123.20'),
            isv=Decimal('25.23'),
            total=Decimal('1230.23'),
            is_completed=False,
            payment_method='Efectivo'
        )
        billing = models.Billing.objects.create(
            id_freight=freight,
            date='2003-12-12',
        )
        commission = models.Commission.objects.create(
            id_billing=billing,
            commission_partner=Decimal('1024.50'),
            commission_traesu=Decimal('1025.23'),
            commission_motorist=Decimal('1026.23'),
            is_payed=True,
        )
        self.assertTrue(commission.id_billing.id, billing.id)
