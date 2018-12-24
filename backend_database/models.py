from django.conf import settings
from django.db import models
from django.utils import timezone # I probably won't use this import, check later


# Create your models here.

# Table includes the information pertaining to the individual items
class Item(models.Model):
    number = models.IntegerField(primary_key=True)
    item_description = models.CharField(max_length=45)
    cost = models.IntegerField()
    item_discontinued = models.BooleanField(default=False)
    name = models.CharField(max_length=45)

# Table includes information about vendor linked to orders
class Vendor(models.Model):
    number = models.IntegerField(primary_key=True)
    vendor_description = models.CharField(max_length=45)

# desciption of physical locations in the laboratory that items are located 
class Locations(models.Model):
    number = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=45)

# a different category that items will be a part on to have better search results when looking for an item
class Categories(models.Model):
    number = models.IntegerField(primary_key=True)
    category_description = models.CharField(max_length=45)

# Table includes information about current and past orders of items
class Orders(models.Model):
    number = models.IntegerField(primary_key=True)
    reorder = models.BooleanField(default=False)
    item_number = models.ForeignKey(Item, on_delete=models.CASCADE) # might not work
    vendor_number = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date_last_order = models.DateTimeField(default=timezone.now)

# main table of the inventory used to view items in stock
class Stock(models.Model):
    number = models.IntegerField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    value = models.FloatField()











