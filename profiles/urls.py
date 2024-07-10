from django.urls import path
from . import views

urlpatterns = [
    path('edit/', views.edit_profile, name='edit_profile'),
    path('', views.my_profile, name='my_profile'),
    path('<int:id>', views.view_profile, name='view_profile'),
    path('<int:id>/projects', views.view_profile_projects, name='view_profile_projects'),
    path('<int:id>/articles', views.view_profile_articles, name='view_profile_articles'),
    path('<int:id>/chatbot', views.view_profile_chatbot, name='view_profile_chatbot'),
    path('<int:profile_id>/chatbot/api', views.chatbot_api, name='chatbot_api')
]
