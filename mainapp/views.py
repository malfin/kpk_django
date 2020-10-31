from django.shortcuts import render

from mainapp.models import Category, Web, Dedic


def index(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'mainapp/catalog.html', context)


def basket(request):
    return render(request, 'mainapp/basket.html')


def catalog_page(request, pk):
    web = Web.objects.filter(category_id=pk)
    dedic = Dedic.objects.filter(category_id=pk)
    context = {
        'web': web,
        'dedic': dedic,
    }
    return render(request, 'mainapp/catalog_page.html', context)
