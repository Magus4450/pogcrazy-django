from django.urls import path
from .views import DetailTemplateView, LoginTemplateView, RegisterTemplateView
app_name = 'account'

urlpatterns = [    
    path('/detail/', DetailTemplateView.as_view(), name="detail"),
    path('/login/', LoginTemplateView.as_view(), name="login"),
    path('/register/', RegisterTemplateView.as_view(), name="register"),
]