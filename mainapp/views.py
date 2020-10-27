from django.shortcuts import render

from mainapp.models import Category, Web


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


def login(request):
    return render(request, 'mainapp/login.html')


def catalog_page(request, pk):
    web = Web.objects.filter(category_id=pk)
    context = {
        'web': web,
    }
    return render(request, 'mainapp/catalog_page.html', context)

