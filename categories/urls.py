from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('Categories/list/', CategoryListView.as_view(), name='category_list'),
    path('Categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('Categories/<int:pk>/detail/', CategoryDetailView.as_view(), name='category_detail'),
    path('Categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('Categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]
