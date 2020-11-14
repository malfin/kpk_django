from django.shortcuts import render

from mainapp.models import Category, Hosting


def index(request):
    context = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    categories = Category.objects.all()
    context = {
        'page_title': 'каталог',
        'categories': categories
    }
    return render(request, 'mainapp/catalog.html', context)


def catalog_page(request, category_pk):
    hosting = Hosting.objects.filter(category_id=category_pk)
    context = {
        'page_title': 'страница услуг',
        'hosting': hosting,
    }
    return render(request, 'mainapp/catalog_page.html', context)
