from django.urls import path
from .views import order_create, order_detail

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('admin/order/<int:order_id>', order_create, name='order_detail'),
]



