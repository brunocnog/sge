from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'title', 'brand', 'category', 'description',
            'serie_number', 'cost_price', 'selling_price', 'quantity'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'serie_number': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Nome',
            'description': 'Descrição',
            'brand': 'Marca',
            'category': 'Categoria',
            'serie_number': 'Número de Série',
            'cost_price': 'Preço de Custo',
            'selling_price': 'Preço de Venda',
            'quantity': 'Quantidade',
        }
