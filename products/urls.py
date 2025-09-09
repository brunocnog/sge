from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView


urlpatterns = [
    path('products/list/', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
