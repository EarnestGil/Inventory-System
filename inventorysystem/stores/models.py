from django.db import models

# Create your models here.
class Branch(models.Model):
    """A store thats part of a parent company"""
    name = models.CharField(
        max_length=70,
        help_text="The store branch's name"
    )
    address_1 = models.CharField(
        max_length=100,
        help_text="Address field 1"
    )
    address_2 = models.CharField(
        max_length=100,
        help_text="Address field 2"
    )
    contact_number = models.CharField(
        max_length=20,
        help_text="The store branch's contact number"
    )

class Product(models.Model):
    """An item that is sold by the store"""
    class ProductTypes(models.TextChoices):
        DOOR = "DOOR", "Door"
        TILE = "TILE", "Tile"
        WINDOW = "WINDOW", "Window"

    name = models.CharField(
        max_length=20,
        help_text="The Product's Name"
    )
    description = models.TextField(
        help_text="The Product's Description"
    )
    type = models.CharField(
        max_length=20,
        choices=ProductTypes.choices,
        verbose_name="Product Type"
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text="The value of the Product when sold on the Store"
    )
    cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text="The value of the Product when bought from the Supplier"
    )

class BranchProducts(models.Model):
    """The \'Associative Entity\' used for the Branch and Product Entity's many to many relationship"""
    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

class Window(models.Model):
    """A Product that is classified as a Window"""
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=20,
        help_text="The Window's Name"
    )
    description = models.TextField(
        help_text="The Window's Description"
    )
