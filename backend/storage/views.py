from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.db.models import Min
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm
from .models import Stock, BoxX


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('storage:auth')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/auth.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('storage:lk')


def logout_user(request):
    logout(request)
    request.session.clear()
    return redirect('storage:index')


def auth(request):
    return render(request, 'user/auth.html')


def registration(request):
    return render(request, 'user/registration.html')


def lk(request):
    return render(request, 'user/lk.html')


def index(request):
    return render(request, 'storage/index.html')


def boxes(request):
    stocks = Stock.objects.all()
    for stock in stocks:
        min_price = BoxX.objects.filter(stock=stock).aggregate(Min('price'))
        stock.min_price = int(min_price['price__min'])
        stock.total_boxes = BoxX.objects.filter(stock=stock).count()
        stock.free_boxes = BoxX.objects.filter(stock=stock, rented=False).count()
    return render(request, 'storage/boxes.html', context={'stocks': stocks})


def faq(request):
    return render(request, 'storage/faq.html')


def price(request):
    return render(request,'storage/price.html')
