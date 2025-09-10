from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Inflow
from .forms import InflowForm


class InflowListView(ListView):
    model = Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    ordering = ['id']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset
    

class InflowCreateView(CreateView):
    model = Inflow
    template_name = 'inflow_create.html'
    form_class = InflowForm
    success_url = reverse_lazy('inflow_list')    


class InflowDetailView(DetailView):
    model = Inflow
    template_name = 'inflow_detail.html'
