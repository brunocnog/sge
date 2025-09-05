from django.urls import path
from .views import BrandListView, BrandCreateView


urlpatterns = [
    path('brands/list/', BrandListView.as_view(), name='brand_list'),
    path('brands/create/', BrandCreateView.as_view(), name='brand_create')
]