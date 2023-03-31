from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField()
    codebar = models.CharField(max_length=20, unique=True)
    

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.slug

class ProductStock(models.Model):
    product = models.ForeignKey(Product, verbose_name=("products"), on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    unit = models.CharField( max_length=10, default='und')
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateField(auto_now_add=False)
    updated_at = models.DateField(auto_now_add=False)
    

    class Meta:
        verbose_name = ("ProductStock")
        verbose_name_plural = ("ProductStocks")

    def __str__(self):
        return self.product.name

    def get_absolute_url(self):
        return self.product.name

