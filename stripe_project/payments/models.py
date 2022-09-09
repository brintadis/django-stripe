from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(
        verbose_name="Item name",
        max_length=255,
    )
    description = models.CharField(
        verbose_name="Description",
        max_length=255,
    )
    price = models.DecimalField(
        verbose_name="Price",
        max_digits=20,
        decimal_places=2,
    )

    def __str__(self) -> str:
        return f'Item: {self.name}, Price: {self.price}'

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'