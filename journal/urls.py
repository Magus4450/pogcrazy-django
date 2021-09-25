from django.urls import path
from .views import journal_view
app_name = 'journal'

urlpatterns = [
    path('', journal_view, name='journal')
]