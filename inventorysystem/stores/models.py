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

class Product(models.model):
    """An item that is sold by the store"""
    type = models.CharField(
        max_length=20,
        help_text="The type of the Product"
    )
    price = models.DecimalField(
        decimal_places=2,
        help_text="The price of the Product when sold on the Store"
    )
    cost = models.DecimalField(
        decimal_places=2,
        help_text="The price of the Product when bought from the Supplier"
    )

class BranchProducts(models.model):
    """The \'Associative Entity\' used for the Branch and the Product Entity's many to many relationship"""
    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
