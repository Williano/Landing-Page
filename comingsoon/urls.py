from django.urls import path
from . import views

app_name = 'comingsoon'

urlpatterns = [
    path('', views.home, name='home'),
]


