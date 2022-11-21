from django.urls import path

from . import views

urlpatterns = [
    #path arguments: route, view, kwargs, name
    #route and view are mandatory
    path('', views.index, name='index'),
]