from django.shortcuts import render
from .forms import OrderCreateForm
from .models import Order
from .models import OrderItem
from cart.cart import Cart

# Create your views here.


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm()
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'], price=item['price'])
            cart.clear()
            return render(request, '../templates/orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, '../templates/orders/create.html', {'form': form, 'cart': cart})




