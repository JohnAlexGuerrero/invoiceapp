from django import forms


from inventory.models import Product
from inventory.models import ProductStock

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ("name","slug","codebar","brand") 

class ProductStockForm(forms.ModelForm):
    cost = forms.DecimalField(label="Costo",initial=1000, decimal_places=2, min_value=0, required=False)
    created_at = forms.DateField(required=False)
    updated_at = forms.DateField(required=False)
    class Meta:
        model = ProductStock
        fields = ("product","stock","unit","cost","created_at","updated_at")
