from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from basketapp.models import HostingBasket
from mainapp.models import Hosting


def index(request):
    items = HostingBasket.objects.filter(user=request.user)
    context = {
        'object_list': items,
    }
    return render(request, 'basketapp/basket.html', context)


def add(request, hosting_id):
    hosting = Hosting.objects.get(pk=hosting_id)
    HostingBasket.objects.get_or_create(
        user=request.user,
        hosting=hosting
    )
    return HttpResponseRedirect(
        reverse('mainapp:catalog_page', kwargs={'category_pk': hosting.category_id})
    )


def remove(request, hosting_basket_id):
    if request.is_ajax():
        hosting = HostingBasket.objects.get(id=hosting_basket_id)
        hosting.delete()
        return JsonResponse({
            'status': '0',
            'text': hosting_basket_id,
        })
