from django.urls import path
from .views import BrandListView, BrandCreateView, BrandDetailView, BrandUpdateView


urlpatterns = [
    path('brands/list/', BrandListView.as_view(), name='brand_list'),
    path('brands/create/', BrandCreateView.as_view(), name='brand_create'),
    path('brands/<int:pk>/detail/', BrandDetailView.as_view(), name='brand_detail'),
    path('brands/<int:pk>/update/', BrandUpdateView.as_view(), name='brand_update'),
]