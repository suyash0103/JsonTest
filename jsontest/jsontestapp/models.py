from django.db import models

# Create your models here.

class Users(models.Model):
    idp = models.CharField(max_length = 9, primary_key = 'True')
    real_name = models.CharField(max_length = 50)
    tz = models.CharField(max_length = 50)

class ActivityPeriod(models.Model):
    idp = models.ForeignKey(Users, on_delete=models.CASCADE)
    activity_periods = models.CharField(max_length = 25)