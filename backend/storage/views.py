from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.management import call_command
from django.db.models import Min
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import LoginUserForm, RegisterUserForm
from .models import BoxX, Stock, Lead, UserProfile


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
    user = User.objects.get(username=request.user.username)
    profile = UserProfile.objects.filter(user=user)
    if profile and profile.boxx:
        context = {'box': profile.boxx}
    else:
        context = {'box': 'На данный момент нет арендованных боксов'}
    return render(request, 'user/lk.html', context=context)


def index(request):
    return render(request, 'storage/index.html')


def boxes(request):
    stocks = Stock.objects.all()
    for stock in stocks:
        min_price = BoxX.objects.filter(stock=stock).aggregate(Min('price'))
        stock.min_price = int(min_price['price__min'])
        stock.total_boxes = BoxX.objects.filter(stock=stock).count()
        stock.free_boxes = BoxX.objects.filter(
            stock=stock, rented=False
        ).count()
    return render(request, 'storage/boxes.html', context={'stocks': stocks})


def faq(request):
    return render(request, 'storage/faq.html')


def price(request):
    email = request.POST.get('email', '')
    address = request.POST.get('address', None)
    phone = request.POST.get('phone', None)
    delivery = True if address else False
    Lead.objects.create(address=address, eMail=email, delivery=delivery, phone=phone)
    return render(request, 'storage/price.html')


def send_emails(request):
    call_command('notify_owners_of_rent_term_ending')

    messages.success(
        request,
        (
            'Система прошла циклом по боксам и отправила'
            ' уведомления тем, у кого истекает срок через месяц'
        ),
    )
    return HttpResponseRedirect(reverse('admin:storage_boxx_changelist'))
