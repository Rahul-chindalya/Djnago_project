from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('prodcuts_list')

class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'