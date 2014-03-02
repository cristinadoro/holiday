from django.db import models
from django.contrib import admin
from django import forms


class Person(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    budget = models.PositiveIntegerField()
    daysoff = models.PositiveIntegerField()
    headshot = models.ImageField(upload_to='tmp',null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

    class Admin:
            pass

class Holiday(models.Model):
    agency = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    nrdays=models.PositiveIntegerField()
    cost=models.PositiveIntegerField()
    infromation=models.CharField(max_length=500)
    website = models.URLField()
    headshot = models.ImageField(upload_to='tmp')

    def __str__(self):
        return '%s,  %s - %d $' % (self.agency, self.destination, self.cost)

    class Admin:
             pass


class Planner(models.Model):
    person = models.ForeignKey(Person)
    destination = models.ManyToManyField(Holiday,related_name='destinations')
    departure_date = models.DateField()


    def __str__(self):
       return '%s, departure: %s to %s ' % (self.person.name, self.departure_date,", ".join([Holiday.country
                                                  for Holiday in self.destination.all()]))

    class Admin:
        pass

# Create your models here.
