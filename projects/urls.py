from django.urls import path
from . import views

urlpatterns = [
    path('<int:project_id>/', views.view_project, name='view_project'),
    path('user/<int:user_id>/projects/', views.user_projects, name='user_projects'),
]