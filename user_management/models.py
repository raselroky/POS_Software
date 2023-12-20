
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    #p_k=models.AutoField(primary_key=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    first_name = models.CharField(max_length=30,null=True,blank=True)
    last_name = models.CharField(max_length=30,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    mobile_number = models.CharField(max_length=20, unique=True,null=True)
    position=models.CharField(max_length=500,null=True,blank=True)
    image=models.ImageField(upload_to='images/',blank=True, null=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # this thing is need to avoid some wird error i didn't figure out
    # so i just didn't show it in serializers.py
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='customuser_set',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='customuser_set',
    )
    #----------------------------------
    def __str__(self):
        return self.email

