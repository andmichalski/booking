# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Hotel(models.Model):
    CLASSES_CHOICES = (("First", "1"), ("Second", "2"), ("Thrid", "3"), ("Fourth", "4"), ("Fifth", "5"))
    name = models.CharField(max_length=100)
    location = models.CharField(max_length= 50)
    standard = models.CharField(max_length=1,choices=CLASSES_CHOICES)

class Room(models.Model):
    hotel_id = models.ForeignKey("Hotel", on_delete=models.CASCADE)
    number_persons = models.IntegerField()
    prize = models.DecimalField(max_digits=6, decimal_places=2)