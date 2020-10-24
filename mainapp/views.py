from django.shortcuts import render

from mainapp.models import Category, Web


def index(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'catalog/index.html', context)


def basket(request):
    return render(request, 'basket/index.html')


def login(request):
    return render(request, 'login/index.html')


def catalog_page(request, pk):
    web = Web.objects.filter(category_id=pk)
    vds = Web.objects.filter(category_id=pk)
    context = {
        'web': web,
        'vds': vds,
    }
    return render(request, 'catalog/catalog_page.html', context)

