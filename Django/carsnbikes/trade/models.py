from django.db import models

class Vehicle(models.Model):
    name = models.TextField()
    contact_number = models.IntegerField()
    vehicle_type = models.TextField()
    brand = models.TextField()
    model_name = models.TextField()
    year_of_purchase = models.TextField()
    kilometers = models.IntegerField()
    color = models.TextField()
    registered_state = models.TextField()
    no_of_owners = models.IntegerField()
    base_price = models.IntegerField()
    mode_of_payment = models.TextField()
