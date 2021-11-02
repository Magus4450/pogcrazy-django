from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class AboutTemplateView(TemplateView):
    template_name = "templates/about.html"