from django.db import models

class ServiceReq(models.Model):
    #services requested
    fire = models.CharField(max_length=50)
    police = models.CharField(max_length=50)
    medical = models.CharField(max_length=50)
    PublicWorks = models.CharField(max_length=50)

    #image 
    image = models.ImageField(default=None)