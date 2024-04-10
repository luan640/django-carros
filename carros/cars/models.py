from django.db import models
from django.contrib.auth.models import User

import uuid

class Brand(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Color(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='cars_brand')
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    plate = models.CharField(max_length=10,blank=True, null=True)
    value = models.FloatField()
    km = models.FloatField()
    auction = models.BooleanField()
    color = models.ForeignKey(Color, on_delete=models.PROTECT, related_name='cars_color')
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    created_by = models.ForeignKey(User, related_name='users', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model