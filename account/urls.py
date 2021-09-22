from django.urls import path
from .views import detail, login, register, logout, addresses
app_name = 'account'

urlpatterns = [    
    path('detail/', detail, name="detail"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('register/', register, name="register"),
    path('addresses/', addresses, name="addresses"),

]