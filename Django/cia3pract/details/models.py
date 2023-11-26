from django.db import models

# Create your models here.

class Details(models.Model):
    name = models.TextField()
    mobile = models.TextField()
