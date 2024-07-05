# orders/models.py
from django.db import models
from django.conf import settings

class CardDesign(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='card_designs/')

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15)
    address = models.TextField()
    card_design = models.ForeignKey(CardDesign, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logos/')
    name_on_card = models.CharField(max_length=150)
    headline_on_card = models.CharField(max_length=255)
    phone_on_card = models.CharField(max_length=15)
    status = models.CharField(max_length=100, default='Pending')
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} by {self.full_name}'
