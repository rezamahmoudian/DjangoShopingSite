from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderCreateForm
from .models import Order
from .models import OrderItem
from cart.cart import Cart
from .tasks import send_mail_func
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'], price=item['price'])
            cart.clear()
            send_mail_func.delay(order.id)
            request.session['order_id'] = order.id
            #
            return redirect(reverse('zarinpal:request'))
            # return render(request, '../templates/orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, '../templates/orders/create.html', {'form': form, 'cart': cart})


@staff_member_required()
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, '../templates/admin/orders/detail.html', {'order': order})
