
from django.urls import *
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
]