from django.contrib import admin
from django.urls import path

from apps.views import CustomLoginView, CustomLogoutView, CustomRegister, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_page'),
    path('login', CustomLoginView.as_view(), name='login_page'),
    path('logout', CustomLogoutView.as_view(), name='logout_page'),
    path('register', CustomRegister.as_view(), name='register_page'),
]
