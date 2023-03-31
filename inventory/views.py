from django.shortcuts import render
from datetime import datetime
from django.db.models import Sum


from django.views import View
from django.views.generic import TemplateView

from inventory.forms import ProductForm
from inventory.forms import ProductStockForm

from inventory.models import Product
from inventory.models import ProductStock

class HomeView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['products'] = products
        context["form"] = ProductForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)

class AddProductStockView(TemplateView):
    template_name = "add_product_stock.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        product = Product.objects.get(slug=self.kwargs['product_slug'])
        list_stocks = ProductStock.objects.select_related('product').filter(product__slug=self.kwargs['product_slug'])
        form_initial = {'product':product,'stock':1, 'created_at':datetime.now(), 'updated_at':datetime.now()}
        
        context["product"] = product
        context["form"] = ProductStockForm(initial=form_initial)
        context["list_stocks"] = list_stocks
        context["avalible"] = ProductStock.objects.aggregate(Sum('stock'))
        # print(context)
        return context
    
    def post(self, request, *args, **kwargs):
        form = ProductStockForm(request.POST)
        if form.is_valid():
          form.save()
        return super().get(request, *args, **kwargs)