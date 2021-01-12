from django.db import models
from django import forms
from django.contrib.auth.models import User
import random

# Create your models here.


class Messages(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True, default='')
    desc = models.TextField(max_length=20000, blank=True, null=True, default='')
    user_email = models.CharField(max_length=50, blank=True, null=True)
    sender = models.CharField(max_length=30, blank=True, null=True)
    pub_date = models.DateTimeField('Data Wysłania', blank=True, null=True)
    def __str__(self):
       return str(self.title)
class Lessons(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True, default='')
    desc = models.TextField(max_length=2500, blank=True, null=True, default='')
    link = models.CharField(max_length=300, blank=True, null=True, default='')
    pub_date = models.DateTimeField('Data publikacji')
    image = models.FileField(upload_to='static/', blank=True, null=True)
    def __str__(self):
        return str(''+ self.title)

class Texts(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True, default='Tytuł sekcji',)
    desc = models.TextField(max_length=15000, blank=True, null=True, default='Opis')
    pub_date = models.DateTimeField('Data publikacji')
    link = models.CharField(max_length=2000, blank=True, null=True, default='')
    link_name = models.CharField(max_length=2000, blank=True, null=True, default='')
    image = models.FileField(upload_to='static/', blank=True, null=True)
    def __str__(self):
       return str(self.title)
