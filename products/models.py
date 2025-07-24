from django.db import models
from categories.models import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True) # Não sei se vou usar
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') # Relacionamento com o modelo de categorias

    # Para desencargo de consciência novamente
    def __str__(self):
        return self.name
