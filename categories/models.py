from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    # Para desencargo de consciência
    def __str__(self):
        return self.name
