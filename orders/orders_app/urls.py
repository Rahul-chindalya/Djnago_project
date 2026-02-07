from django.urls import path
from . import views

urlpatterns=[
    path('products/add/',views.ProductCreateView.as_view(),name='add_product'),
    path('product/list/',views.ProductListView.as_view(),name='products_list')
]