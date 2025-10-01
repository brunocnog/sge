from django.urls import path
from .views import InflowListView, InflowCreateView, InflowDetailView, InflowCreateListAPIView, InflowRetrieveAPIView


urlpatterns = [
    path('inflows/list/', InflowListView.as_view(), name='inflow_list'),
    path('inflows/create/', InflowCreateView.as_view(), name='inflow_create'),
    path('inflows/<int:pk>/detail/', InflowDetailView.as_view(), name='inflow_detail'),
    path('api/v1/inflows/', InflowCreateListAPIView.as_view(), name='inflow-create-list-api-view'),
    path('api/v1/inflows/<int:pk>/', InflowRetrieveAPIView.as_view(), name='inflow-detail-api-view'),
]
