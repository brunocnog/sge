from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Brand
from .forms import BrandForm


class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    ordering = ['id']
    paginate_by = 10
    permission_required = 'brands.view_brand'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
    

class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Brand
    template_name = 'brand_create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')
    permission_required = 'brands.add_brand'


class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Brand
    template_name = 'brand_detail.html'
    permission_required = 'brands.view_brand'


class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Brand
    template_name = 'brand_update.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')
    permission_required = 'brands.change_brand'

class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand_list')
    permission_required = 'brands.delete_brand'
    