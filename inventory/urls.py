from django.urls import path

from inventory.views import HomeView
from inventory.views import AddProductStockView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug:product_slug>/add', AddProductStockView.as_view(), name='add_product_stock'),
]
