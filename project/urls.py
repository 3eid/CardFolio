from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('main.urls')),
    path('orders/', include('orders.urls')),
    path('profiles/', include('profiles.urls')),
    path('projects/', include('projects.urls')),
    path('articles/', include('blogs.urls')),
    path('chatbot/', include('chatbot.urls')),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
