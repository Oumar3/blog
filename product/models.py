from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    describe = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self) -> str:
        return self.title
