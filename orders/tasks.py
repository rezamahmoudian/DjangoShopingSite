from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task()
def send_mail_func(order_id):
    order = Order.objects.get(id=order_id)
    #operations
    mail_subject = f"order {order.id}"
    message = f"hi {order.first_name} your order is ready.\nthank you for your shopping"
    to_email = order.email
    mail_sent = send_mail(
        subject=mail_subject,
        message=message,
        from_email='admin@gmail.com',
        recipient_list=[to_email],
        fail_silently=True,
    )
    return mail_sent