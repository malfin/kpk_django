from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    return render(request, 'catalog/index.html')


def basket(request):
    return render(request, 'basket/index.html')


# Create your views here.
