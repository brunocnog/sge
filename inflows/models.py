from django.db import models
from suppliers.models import Supplier
from products.models import Product


class Inflow(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='inflows', verbose_name='Fornecedor')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='inflows', verbose_name='Produto')
    quantity = models.IntegerField(default=0, verbose_name='Quantidade')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última atualização')

    class Meta:
        verbose_name = 'Entrada de Produto'
        ordering = ['-created_at']

    def __str__(self):
        return str(self.product)
