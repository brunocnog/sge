from django.db import models
from brands.models import Brand
from categories.models import Category



class Product(models.Model):
    title = models.CharField(max_length=500, verbose_name='Produto')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products', verbose_name='Marca')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name='Categoria')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    serie_number = models.CharField(max_length=200, null=True, blank=True, verbose_name='Número de Série')
    cost_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Preço de custo')
    selling_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Preço de venda')
    quantity = models.IntegerField(default=0, verbose_name='Quantidade')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Atualização')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
