from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator


class FirstCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, blank=False)
    price = models.IntegerField(unique=False, blank=False, validators=[
        MinValueValidator(0)
    ])
    description = models.CharField(max_length=255, unique=False, blank=False)


class SecondCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, blank=False)
    price = models.IntegerField(unique=False, blank=False, validators=[
        MinValueValidator(0)
    ])
    description = models.CharField(max_length=255, unique=False, blank=False)


class Dessert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, blank=False)
    price = models.IntegerField(unique=False, blank=False, validators=[
        MinValueValidator(0)
    ])
    description = models.CharField(max_length=255, unique=False, blank=False)


class Drink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, blank=False)
    price = models.IntegerField(unique=False, blank=False, validators=[
        MinValueValidator(0)
    ])
    description = models.CharField(max_length=255, unique=False, blank=False)
