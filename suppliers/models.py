from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=500, verbose_name='Nome')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última atualização')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
