from django.db import models


# Unideal - layout due to import constrait
class stocks(models.Model):
    company = models.CharField(max_length=100)
    ticker = models.CharField(max_length=30)
    animal_testing = models.BooleanField()
    nuclear_war = models.BooleanField()
    coal_power = models.BooleanField()
    rainforest_destruction = models.BooleanField()

