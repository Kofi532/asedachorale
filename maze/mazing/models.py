from django.db import models

class Participant(models.Model):
    firstname= models.CharField(max_length=100)
    middlename= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    email= models.CharField(max_length=200)
    timeIn= models.DateTimeField(max_length=200)
    timeOut= models.DateTimeField(max_length=200)
    uniqueid= models.CharField(max_length=100, default='0')
