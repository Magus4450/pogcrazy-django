from django.shortcuts import render


from django.views.generic import TemplateView

class HomeTemplateView(TemplateView):

    template_name = "templates/index.html"
