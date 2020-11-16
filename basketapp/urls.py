import basketapp.views as basketapp
from django.urls import path

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='index'),
    path('add/<int:hosting_id>/', basketapp.add, name='add'),
    path('remove/<int:hosting_basket_id>/', basketapp.remove, name='remove'),
]
