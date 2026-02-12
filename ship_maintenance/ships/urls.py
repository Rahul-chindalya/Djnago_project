from django.urls import path
from . import views

urlpatterns = [
    path('ships/list/',views.ship_list),
    path('ships/create/',views.ship_create),
    path('ships/details/<int:id>',views.ship_detail),
    path('ships/update/<int:id>',views.ship_update),
    path('ships/delete/<int:id>',views.ship_delete),   
]