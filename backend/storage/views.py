from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import LoginUserForm, RegisterUserForm


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration.html' # link to registration form
    success_url = reverse_lazy('auth')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'auth.html' # link to authorization form

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('lk') #  link to user page


def logout_user(request):
    logout(request)
    request.session.clear()
    return redirect('index')


def lk(request):
    return render(request, 'storage/lk.html')


def index(request):
    return render(request, 'storage/index.html')


def boxes(request):
    return render(request, 'storage/boxes.html')


def faq(request):
    return render(request, 'storage/faq.html')
