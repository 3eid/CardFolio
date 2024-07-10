from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:profile_id>/articles/', views.user_articles, name='user_articles'),
    path('<int:article_id>/view/', views.view_article, name='view_article'),
]
