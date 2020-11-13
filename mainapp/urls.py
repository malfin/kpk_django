from django.conf.urls.static import static

import mainapp.views as mainapp
from django.urls import path
from kpk import settings

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('catalog/', mainapp.catalog, name='catalog'),
    path('catalog/category/<int:pk>/', mainapp.catalog_page, name='catalog_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
