from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls import handler404, handler500

from django.conf import settings as django_settings
from django.conf.urls.static import static

from . import views

app_name = 'kynsi'
urlpatterns = [
    url("", views.MainView.as_view(), name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)