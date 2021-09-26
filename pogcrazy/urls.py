
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('home.urls', namespace='home')),
    path('account/', include('account.urls', namespace='account')),
    path('journal/', include('journal.urls', namespace='journal')),
    path('shop/', include('shop.urls', namespace='shop')),
]
