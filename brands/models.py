from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=500, verbose_name='Marca')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última atualização')

    class Meta:
        verbose_name = 'Marca'
        ordering = ['name']

    def __str__(self):
        return self.name
