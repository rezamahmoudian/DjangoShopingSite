from django.shortcuts import render, get_object_or_404, redirect
from .forms import CartAddProductForm
from .cart import Cart
from shop.models import Product
from django.views.decorators.http import require_POST


# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'])
    return redirect('cart:cart_details')