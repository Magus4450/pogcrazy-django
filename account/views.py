from .models import UserAddress
from .forms import AddressForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import TemplateView
from .forms import RegisterForm, LoginForm
from .models import UserInfo
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.decorators import login_required


def logout(request):
    dj_logout(request)
    return redirect(reverse_lazy('account:login'))


def login(request):

    if request.method == "GET":
        form = LoginForm()
    elif request.method == "POST":
        print("IN POST")
        form = LoginForm(request.POST)
        if form.is_valid():
            print("VALIDATED")

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            print(f'Username: {username}, pass: {password}')

            user = authenticate(
                username=username,
                password=password
            )
            print(user)
            if user:
                print(f"LOGGED IN AS {user.first_name}")
                dj_login(request, user)
                return redirect(reverse_lazy('account:detail'))
            else:
                print("Credential dont match")

    return render(request, 'templates/login.html', {'form': form})


def register(request):
    if request.method == "GET":
        form = RegisterForm()

    elif request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = UserInfo(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            # user.set_password(form.cleaned_data['password1'])
            user.set_password(form.cleaned_data['password1'])
            user.save()

            return redirect(reverse_lazy('account:login'))

    return render(request, 'templates/register.html', {'form': form})


@login_required(login_url=reverse_lazy('account:login'))
def detail(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'templates/account.html', context)


@login_required(login_url=reverse_lazy('account:login'))
def addresses(request, pk=None):
    if request.method == "GET":
        if pk:
            address = UserAddress.objects.get(id=pk)
            address.delete()
            return redirect(reverse_lazy('account:addresses'))
        else:
            form = AddressForm()
            data = UserAddress.objects.all()

            context = {
                'form': form,
                'data': data
            }

            return render(request, 'templates/addresses.html', context)

    elif request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = UserAddress(
                user=request.user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone=form.cleaned_data['phone'],
                address1=form.cleaned_data['address1'],
                address2=form.cleaned_data['address2'],
                zipcode=form.cleaned_data['zipcode'],
                country=form.cleaned_data['country'],
                default=form.cleaned_data['default'],
            )
            # user.set_password(form.cleaned_data['password1'])
            address.save()

        return(redirect(reverse_lazy('account:addresses')))
