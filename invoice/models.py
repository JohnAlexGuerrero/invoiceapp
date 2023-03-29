from django.db import models

class Invoice(models.Model):
    number = models.CharField(max_length=50, unique=True)
    created_at = models.DateField( auto_now_add=False)
    expiration_at = models.DateField(auto_now_add=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    

    class Meta:
        verbose_name = ("Invoice")
        verbose_name_plural = ("Invoices")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Invoice_detail", kwargs={"pk": self.pk})

