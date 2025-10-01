from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView, CategoryCreateListAPIView, CategoryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('Categories/list/', CategoryListView.as_view(), name='category_list'),
    path('Categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('Categories/<int:pk>/detail/', CategoryDetailView.as_view(), name='category_detail'), path('Categories/<int:pk>/update/',
                                                                                                    CategoryUpdateView.as_view(), name='category_update'), path('Categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('api/v1/categories/', CategoryCreateListAPIView.as_view(), name='category-create-list-api-view'),
    path('api/v1/categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail-api-view'),
]
