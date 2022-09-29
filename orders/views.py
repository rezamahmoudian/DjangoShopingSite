from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from .forms import OrderCreateForm
from .models import Order
from .models import OrderItem
from cart.cart import Cart
from .tasks import send_mail_func
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from weasyprint import HTML, CSS, pdf
from django.shortcuts import HttpResponse
from django.conf import settings

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
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, '../templates/admin/orders/detail.html', {'order': order})


@staff_member_required()
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    pdf_html = render_to_string('../templates/admin/orders/pdf.html', {"order": order})
    pdf_file = HTML(string=pdf_html).write_pdf(stylesheets=[CSS(settings.STATIC_ROOT + 'css/pdf.css')])

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'filename=Order {order.id}.pdf'
    return response
