from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Supplier
from .forms import SupplierForm


class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    ordering = ['id']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
    

class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    template_name = 'supplier_create.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list')    


class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model =Supplier
    template_name = 'supplier_update.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list')

class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier_list')
