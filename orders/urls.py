from django.urls import path
from .views import order_crate

app_name = 'orders'

urlpatterns = [
    path('create/', order_crate, name='order_create')

]



