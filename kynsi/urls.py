from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls import handler404, handler500

from django.conf import settings as django_settings
from django.conf.urls.static import static

from . import views

app_name = 'kynsi'
urlpatterns = [
    url(r'^$', views.MainView.as_view(), name="index"),
    url(r'^dress-code/$', views.DressCodeView.as_view(), name="dress-code"),
] + static(django_settings.MEDIA_URL, document_root=django_settings.MEDIA_ROOT)