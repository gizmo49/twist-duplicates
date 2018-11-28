from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .import views 

urlpatterns = [
    path('', views.showvideo),
    path('comparevid', views.compare_videofiles, name="comparevids"),

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

