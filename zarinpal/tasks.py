from django.template.loader import render_to_string

from orders.models import Order
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from celery import shared_task
import weasyprint
from django.conf import settings
from io import BytesIO


@shared_task
def send_order_pdf_mail(order_id):
    order = get_object_or_404(Order, id=order_id)
    subject = f'Your Order _ id={order_id}'
    message = 'We sent your order detail for you\nPlease check attached invoice'

    email = EmailMessage(subject, message, "admin@admin.com", order.email)
    html = render_to_string('../templates/admin/orders/pdf.html', {"order": order})
    stylesheets = weasyprint.CSS(settings.STATIC_ROOT + 'css/order_pdf.css')
    out = BytesIO
    weasyprint.HTML(html).write_pdf(out, stylesheets)
    email.attach(f'order_{order_id}', out.getvalue(), 'application/pdf')
    email.send()

