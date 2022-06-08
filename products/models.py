from django.db import models
from django.forms import FloatField, IntegerField


class Silla(models.Model):
    color = models.CharField(max_length=20)
    altura = models.FloatField()
    material = models.CharField(max_length=30)
    precio = models.FloatField()
    stock = models.BooleanField()


class Escritorio(models.Model):
    color = models.CharField(max_length=20)
    altura = models.FloatField()
    material = models.CharField(max_length=30)
    precio = models.FloatField()
    stock = models.BooleanField()


class Mesa (models.Model):
    color = models.CharField(max_length=20)
    altura = models.FloatField()
    material = models.CharField(max_length=30)
    precio = models.FloatField()
    stock = models.BooleanField()


class Sillon (models.Model):
    color = models.CharField(max_length=20)
    altura = models.FloatField()
    material = models.CharField(max_length=30)
    precio = models.FloatField()
    stock = models.BooleanField()
