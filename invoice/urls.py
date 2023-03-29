from django.urls import path

from invoice.views import *

urlpatterns = [
    path('', InvoiceListView.as_view(), name='invoice_list'),
    path('add/', AddInvoiceView.as_view(), name='invoice_add'),
]
