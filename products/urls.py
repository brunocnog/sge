from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductCreateListAPIView, ProductRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('products/list/', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('api/v1/products/', ProductCreateListAPIView.as_view(), name='product-create-list-api-view'),
    path('api/v1/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail-api-view'),
]
