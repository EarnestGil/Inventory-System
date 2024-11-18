from django.db import models

# Create your models here.
class Branch(models.Model):
    """A store thats part of a parent company"""
    name = models.CharField(
        max_length=70,
        help_text="The store branch's name"
    )
    address_1 = models.CharField(
        max_length=100
        help_text="Address field 1"
    )
    address_2 = models.CharField(
        max_length=100
        help_text="Address field 2"
    )
    contact_number = models.CharField(
        max_length=20
        help_text="The store branch's contact number"
    )
