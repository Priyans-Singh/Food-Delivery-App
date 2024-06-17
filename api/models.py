from django.db import models

# Create your models here.

class Option(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    # list = models.ForeignKey(OptionList, on_delete=models.CASCADE, blank=True, null=True) 

class OptionList(models.Model):
    name = models.CharField(max_length=255)
    options = models.ManyToManyField(Option)  # This is a list of options

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    optionslists = models.ManyToManyField(OptionList, blank=True, symmetrical=False) # This is a list of option lists

class CartItem(models.Model):
    date = models.DateTimeField(auto_now=True, blank=True, null=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    addOns = models.ManyToManyField(Option, blank=True, symmetrical=False) # This is a list of options
    totalPrice = models.FloatField(null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Cart(models.Model):
    date = models.DateTimeField(auto_now=True)
    cartItems = models.ManyToManyField(CartItem, blank=True, symmetrical=False) 
    totalQuantity = models.IntegerField(default=0);
    grandTotal = models.FloatField(default=0.0)

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total = models.FloatField()
    isPaid = models.BooleanField(default=True)
    items = models.ManyToManyField(CartItem)
    
