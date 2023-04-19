"""
Database models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)

    dni = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    rtn = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Partner(models.Model):
    """Partner in the system"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    rtn = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=255, blank=True)
    dni = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name


class Motorist(models.Model):
    """Motorist in the system"""
    id_partner = models.ForeignKey('Partner', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    rtn = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=255, blank=True)
    dni = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name


class Truck(models.Model):
    """Truck in the system"""
    id_partner = models.ForeignKey('Partner', on_delete=models.CASCADE)
    truck_number = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.truck_number


class Client(models.Model):
    """Client in the system"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    rtn = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.first_name


class Freight(models.Model):
    id_client = models.ForeignKey('Client', on_delete=models.CASCADE)
    id_partner = models.ForeignKey('Partner', on_delete=models.CASCADE)
    id_motorist = models.ForeignKey('Motorist', on_delete=models.CASCADE)
    id_truck = models.ForeignKey('Truck', on_delete=models.CASCADE)
    supervisor_client = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=255)
    sub_total = models.DecimalField(max_digits=6, decimal_places=2)
    importe_gravado = models.DecimalField(max_digits=6, decimal_places=2)
    isv = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    is_completed = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Billing(models.Model):
    id_freight = models.ForeignKey('Freight', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)


class Commission(models.Model):
    id_billing = models.ForeignKey('Billing', on_delete=models.CASCADE)
    commission_partner = models.DecimalField(max_digits=6, decimal_places=2)
    commission_traesu = models.DecimalField(max_digits=6, decimal_places=2)
    commission_motorist = models.DecimalField(max_digits=6, decimal_places=2)
    is_payed = models.BooleanField(default=False)
