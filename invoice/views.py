from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView

class InvoiceListView(TemplateView):
    template_name = "invoice_list.html"

class AddInvoiceView(TemplateView):
    template_name = "add_invoice.html"
