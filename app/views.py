import json
from django.shortcuts import render
# from .metrics import get_product_metrics, get_sales_metrics, get_daily_sales_data, get_daily_sales_quantity_data
from . import metrics

def home(request):
    product_metrics = metrics.get_product_metrics()
    sales_metrics = metrics.get_sales_metrics()
    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()

    context = {
        'product_metrics': product_metrics,
        'sales_metrics': sales_metrics,
        'daily_sales_data': json.dumps(daily_sales_data),
        'daily_sales_quantity_data':json.dumps(daily_sales_quantity_data),
    }

    return render(request, 'home.html', context)
