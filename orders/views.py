from django.shortcuts import render
from .forms import OrderCreateForm
from .models import Order
from .models import OrderItem
from cart.cart import Cart

# Create your views here.


def order_crate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm()
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'], price=item['price'])
            return render(request, 'templates/orders/order/create.html', {'order': order})
        else:
            form = OrderCreateForm()
        return render(request, 'templates/orders/order/create.html', {'form': form, 'cart': cart})




