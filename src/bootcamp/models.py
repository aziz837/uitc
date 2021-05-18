from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save




class Courser(models.Model):
    name    = models.CharField(max_length=50)
    desc    = models.TextField()
    photo   = models.ImageField(upload_to='profile', null=True)
    price   = models.CharField(max_length=50)



class Person(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE )
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    phone       = models.CharField(max_length=20)
    email       = models.EmailField()
    password    = models.CharField(max_length=15, null=True)
    photo       = models.ImageField(upload_to='profile', null=True)
    courser     = models.ForeignKey(Courser, on_delete=models.CASCADE, null=True, blank=True)
    payment_date = models.CharField(max_length=50, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now=True, blank=True)




    
    
