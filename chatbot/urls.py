from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:profile_no>/', views.update_chatbot, name='update_chatbot'),
]
