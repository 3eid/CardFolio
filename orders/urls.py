# orders/urls.py
from django.urls import path
from .views import order_card_view,track_orders_view

urlpatterns = [
    path('order/', order_card_view, name='order_card'),
     path('', track_orders_view, name='orders'),
]

