from apps.cart.cart import Cart
from .models import Order, OrderItem
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
def checkout(request, first_name, last_name, email, hostel, room, phone,amount):
    order = Order.objects.create(first_name = first_name, last_name = last_name, phone = phone, email = email,hostel = hostel, room = room, paid_ammount = amount)

    for item in Cart(request):
        OrderItem.objects.create(order = order, product = item['product'], vendor = item['product'].vendor, price = item['product'].price, quantity = item['quantity'])
        order.vendor.add(item['product'].vendor)
    return order

def notify_vendor(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    for vendor in order.vendors.all():
        to_email = vendor.created_by.email
        subject = 'New order'
        text_content = 'You have a new order!'
        html_content = render_to_string('order/email_notify_vendor.html', {'order': order, 'vendor': vendor})

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

def notify_customer(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    to_email = order.email
    subject = 'Order confirmation'
    text_content = 'Thank you for the order!'
    html_content = render_to_string('order/email_notify_customer.html', {'order': order})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()