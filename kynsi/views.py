from django.template import RequestContext, loader
from django.http import HttpResponse, JsonResponse
from django.template.context_processors import csrf
from django.http.response import Http404
import requests, json
from django.db.models import Q
from django.shortcuts import render, redirect
from django.conf import settings as django_settings
from django.views.generic import FormView
from django.core.mail import send_mail, BadHeaderError

from .models import *

def default_context(request, alias, object):
    try:
        data = object.objects.get(alias=alias)
    except:
        raise Http404

    c = {}
    c.update(csrf(request))

    context_object = {
        'data': data,
        'c': c,
    }

    return context_object


class SiteGenericView(FormView):
    """
    Общие настройки сайта
    """
    template_name = None
    site_settings = None

    def get_context_data(self, **kwargs):
        context = {
            'site_settings': Site.objects.first(),
            'salons': Salons.objects.all()
        }
            
        return context


class MainView(SiteGenericView):
    """
    Главная страница
    """
    template_name = "index.html"
    

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)

        context['categories'] = Categories.objects.all().filter(is_show=True)
        context['brands'] = Brands.objects.all().filter(is_show=True)
        context['salonsliders'] = SalonsSlider.objects.all().first()
        context['blogliders'] = BlogSlider.objects.all().filter(is_show=True)
        context['reviewssliders'] = ReviewsSlider.objects.all().filter(is_show=True)

        return self.render_to_response(context)


class DressCodeView(SiteGenericView):
    """
    Страница дресскод
    """
    template_name = "dresscode.html"

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)


def sendmail(request):
    if request.is_ajax():
        name = request.POST.get('name','')
        phone = request.POST.get('phone','')
        nominal = request.POST.get('nominal','')
        utm = request.POST.get('utm','')
        
        message_html = u'Заказ Сертификата с сайта kynsi.ru <br/>От ' + name + u' <br/>Телефон: ' + phone + '<br/>Номинал: ' + nominal + '<br/>Реклама: ' + utm + '.'
        recipient_list = ['Yulia.d@kynsi.ru']

        try:
            send_mail(
                u'Заказ сертификата на сайте kynsi.ru', message_html, 'kynsi-sert@yandex.ru', recipient_list,
                html_message=message_html, fail_silently=False)
        except (BadHeaderError, AttributeError):  # Защита от уязвимости
            error = 'Invalid header found'
        # Переходим на другую страницу, если сообщение отправлено

    return HttpResponse('ok')

