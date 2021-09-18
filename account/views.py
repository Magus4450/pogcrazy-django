from django.shortcuts import render

from django.views.generic import TemplateView

class LoginTemplateView(TemplateView):

    template_name = 'account/login.html'

class RegisterTemplateView(TemplateView):

    template_name = 'account/register.html'

class DetailTemplateView(TemplateView):

    template_name = 'account/account.html'
