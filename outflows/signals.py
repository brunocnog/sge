from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Outflow
from services.notify import Notify
from datetime import datetime


@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()


@receiver(post_save, sender=Outflow)
def send_outflow_event(sender, instance, created, **kwargs):
    try:
        if created:
            notify = Notify()

            data = {
                'event_type': 'create_outflow',
                'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                'product': instance.product.title,
                'product_cost_price': float(instance.product.cost_price),
                'product_selling_price': float(instance.product.selling_price),
                'quantity': instance.quantity,
                'description': instance.description,
            }

            notify.send_order_event(data)
    except:
        pass
