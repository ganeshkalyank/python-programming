from django.db import models

# Create your models here.

class Member(models.Model):
    AadharNumber = models.TextField()
    Name = models.TextField()
    Age = models.TextField()
    Address = models.TextField()
    NativePlace = models.TextField()
    MobileNumber = models.TextField()
