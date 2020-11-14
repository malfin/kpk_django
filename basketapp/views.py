from django.http import HttpResponseRedirect
from django.shortcuts import render

from basketapp.models import HostingBasket
from mainapp.models import Hosting


def index(request):
    return render(request, 'basketapp/basket.html')


def add(request, hosting_id):
    hosting = Hosting.objects.get(pk=hosting_id)
    HostingBasket.objects.get_or_create(
        user=request.user,
        hosting=hosting
    )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
