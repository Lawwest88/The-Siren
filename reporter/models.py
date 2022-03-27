from django.db import models

class Reporter(models.Model):

    #user info
    first_name  = models.CharField(max_length=100)
    last_name   = models.CharField(max_length=100)
    User_email  = models.EmailField(max_length=125,blank=True,unique=True)
    age = models.IntegerField(null=True)
