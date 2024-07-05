from django.urls import path
from . import views

urlpatterns = [
    path('edit/', views.edit_profile, name='edit_profile'),
    path('', views.view_profile, name='view_profile'),
]
