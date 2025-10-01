from django.urls import path
from .views import OutflowListView, OutflowCreateView, OutflowDetailView, OutflowCreateListAPIView, OutflowRetrieveAPIView


urlpatterns = [
    path('outflows/list/', OutflowListView.as_view(), name='outflow_list'),
    path('outflows/create/', OutflowCreateView.as_view(), name='outflow_create'),
    path('outflows/<int:pk>/detail/', OutflowDetailView.as_view(), name='outflow_detail'),

    path('api/v1/outflows/', OutflowCreateListAPIView.as_view(), name='outflow-create-list-api-view'),
    path('api/v1/outflows/<int:pk>/', OutflowRetrieveAPIView.as_view(), name='inflow-detail-api-view'),
]
