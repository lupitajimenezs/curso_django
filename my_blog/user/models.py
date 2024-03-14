#PARA HACER UN OVERRIDE DEL USUARIO

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique = True)
    web_site = models.CharField(max_length = 255, blank = True)
    twitter = models.CharField(max_length = 255, blank = True)

    #CONFIGURANDO INICIO DE SESSION CON CORREO
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
