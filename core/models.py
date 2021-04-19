from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    class Types(models.TextChoices):
        CLINIC = 'CLINIC', 'Clinic'
        PATIENT = 'PATIENT', 'Patient'
    

    type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.PATIENT)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Clinic(models.Model):
    """Clinic for patients"""
    cname = models.CharField(max_length=255)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    @property
    def owner_id(self):
        return self.user.pk

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.CLINIC
            return super().save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.name


class Reservation(models.Model):
    """Reservation object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(auto_now=True)
    clinic = models.ForeignKey(
        'Clinic',
        on_delete=models.CASCADE
    )
    up_date = models.DateTimeField()
    comment = models.TextField(blank=True)
    canceled = models.BooleanField(default=False)

    class Meta:
        unique_together = ['up_date', 'clinic']

    def __str__(self):
        return f'{self.clinic} {self.up_date}'
