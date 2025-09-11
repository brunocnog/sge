from django.shortcuts import render
from .metrics import get_product_metrics

def home(request):
    product_metrics = get_product_metrics()

    context = {
        'product_metrics': product_metrics
    }

    return render(request, 'home.html', context)