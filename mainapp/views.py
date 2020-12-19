from django.shortcuts import render
from django.views.generic import ListView

from mainapp.models import Category, Hosting


class PageTitleMixin:
    page_title = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['page_title'] = self.page_title
        return context


def index(request):
    context = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


class CatalogListView(PageTitleMixin, ListView):
    model = Category
    page_title = 'каталог'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=object_list, **kwargs)
    #     context['page_title'] = 'каталог'
    #     return context


def catalog_page(request, category_pk):
    hosting = Hosting.objects.filter(category_id=category_pk)
    context = {
        'page_title': 'страница услуг',
        'hosting': hosting,
    }
    return render(request, 'mainapp/catalog_page.html', context)
