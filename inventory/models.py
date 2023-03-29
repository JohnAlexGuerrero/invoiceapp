from django.db import models

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
        return reverse("Product_detail", kwargs={"pk": self.pk})
