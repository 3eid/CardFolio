# from django.db import models

# class CardDesign(models.Model):
#     name = models.CharField(max_length=100)
#     # Add other fields like image, description, etc.
#     image = models.ImageField()
    

# class Order(models.Model):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     card_design = models.ForeignKey(CardDesign, on_delete=models.PROTECT)
#     # Add other fields like shipping address, order date, etc.
