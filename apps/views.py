from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView

from apps.forms import UserRegisterModelForm
from apps.models import Product
from apps.tasks import send_to_email


# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'apps/auth/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('product_list_page')


class CustomLogoutView(View):
    template_name = 'apps/auth/login.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('product_list_page')


class CustomRegister(CreateView):
    form_class = UserRegisterModelForm
    template_name = 'apps/auth/register.html'
    success_url = reverse_lazy('product_list_page')

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        user = form.save()
        send_to_email.delay('Saytimizga xush kelibsiz!', form.cleaned_data['email'])
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class ProductListView(ListView):
    model = Product
    template_name = 'apps/product/product-list.html'
    context_object_name = 'products'
