from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    license_plate = models.IntegerField()
    year = models.IntegerField()

class Person(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    birth_date = models.DateField()
    occupation = models.CharField(max_length=40)

class House_pet(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    birth_date = models.DateField()
    animal = models.CharField(max_length=40)
    breed = models.CharField(max_length=40)
    
class Money(models.Model):
    type = models.CharField(max_length=40)
    amount = models.IntegerField()
    
