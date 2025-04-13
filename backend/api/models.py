from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} (x{self.quantity})"
