from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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
    return HttpResponseRedirect(reverse('mainapp:catalog_page',
                                        kwargs={'category_pk': hosting.category_id}))
