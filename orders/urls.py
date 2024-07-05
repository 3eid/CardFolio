# orders/urls.py
from django.urls import path
from .views import order_card_view, order_success_view,track_orders_view

urlpatterns = [
    path('order/', order_card_view, name='order_card'),
    path('order-success/', order_success_view, name='order_success'),
     path('track/', track_orders_view, name='track_orders'),
]

