from django.db import models

# Create your models here.

class PlantDetails(models.Model):
    plant_name = models.TextField()
    plant_type = models.TextField()
    plant_price = models.TextField()
    plant_benefits = models.TextField()
