from django.urls import path
from .views import product_view
app_name = 'shop'

urlpatterns = [
    path('product/<int:pk>', product_view, name='product')
]