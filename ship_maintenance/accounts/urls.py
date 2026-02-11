from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.user_register),
    path('login/',views.user_login),
    path('users/list/',views.users_list),
    path('users/<int:id>/detail/',views.user_detail),
    path('users/<int:id>/update/',views.user_update),
    path('users/<int:id>/delete/',views.user_delete),
    path('test/',views.test_auth),
]