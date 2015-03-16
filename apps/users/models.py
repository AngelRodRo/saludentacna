# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff,
                     is_superuser, **extra_fields):
        if not email:
            raise  ValueError('El email es obligatorio')
        email= self.normalize_email(email)
        user= self.model(username=username, email=email, is_active=True,
                         is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,username,email,password=None,**extra_fields):
        return self._create_user(username,email,password,False,False,**extra_fields)
    def create_superuser(self,username,email,password,**extra_fields):
        return self._create_user(username,email,password,True,True,**extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email=models.EmailField(max_length=50)
    first_name=models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    avatar=models.URLField()

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.first_name+' '+self.last_name

class Pais(models.Model):
    pais = models.CharField(verbose_name='pais', max_length=5)

    class Meta:
        verbose_name_plural = 'Paises'

    def __unicode__(self):
        return self.pais

class Ciudad(models.Model):
    ciudad = models.CharField(verbose_name='ciudad', max_length=15)
    pais = models.ForeignKey(Pais, default='',blank=False)
    class Meta:
        verbose_name_plural = 'Ciudades'

    def __unicode__(self):
        return self.ciudad

class Cliente(models.Model):
    usuario = models.OneToOneField(User)
    dni = models.CharField(verbose_name='DNI', max_length=30,primary_key=True)
    telefono= models.CharField(verbose_name='Telefono',null=True,
                                blank=True,max_length=15)
    # pais = models.ForeignKey(Pais)
    ciudad = models.ForeignKey(Ciudad)

    class Meta:
        verbose_name_plural = 'Clientes'

    def __unicode__(self):
        return self.first_name+' '+self.last_name

