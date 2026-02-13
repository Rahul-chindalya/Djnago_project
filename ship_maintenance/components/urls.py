from django.urls import path
from . import views

urlpatterns =[
    path('components/create/',views.component_create),
    path('components/list/',views.components_list),
    path('components/details/<int:id>/',views.components_detail),
    path('components/update/<int:id>/',views.components_update),
    path('components/delete/<int:id>/',views.component_delete),
]