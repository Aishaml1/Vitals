from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.

from django.db import models


SEX_CHOICES= [
    ('female', 'Male'),
    ('female', 'Female'),
    ('x', 'X'),
   
    ]
class Patients(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    sex = forms.CharField(label='sex:', widget=forms.Select(choices=SEX_CHOICES))
    dob = models.DateField(max_length=8)

user = models.ForeignKey(User, on_delete=models.CASCADE)