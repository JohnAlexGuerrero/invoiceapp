from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = ("Provider")
        verbose_name_plural = ("Providers")
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.name

class Bill(models.Model):
    provider = models.ForeignKey(Provider, verbose_name=("providers"), on_delete=models.CASCADE)
    number = models.CharField(max_length=50, unique=True)
    created_at = models.DateField()
    expiration_at = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = ("Bill")
        verbose_name_plural = ("Bills")

    def __str__(self):
        return f'{self.provider.name} {self.number}'

    def get_absolute_url(self):
        return self.provider.name

