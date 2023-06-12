from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("decord",views.decord,name='decord'),
    path("americano",views.americano,name='americano'),
    path("caffeMac",views.caffeMac,name='caffemac'),

    path("greenCoffe",views.greenCoffe,name='greenCoffe'),

    path("coldCoffe",views.coldCoffe,name='coldCoffe'),
    path("",views.index,name='home')
]
