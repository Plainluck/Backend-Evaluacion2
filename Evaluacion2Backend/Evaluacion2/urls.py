"""Evaluacion2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PokeTCG import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    

    #urls cards#
    path('', views.card_list , name='card_list'),
    path('cards/<int:pk>/', views.card_detail, name='card_detail'),
    path('cards/new/', views.card_add, name='card_add'),
    path('cards/<int:pk>/edit/', views.card_edit, name='card_edit'),
    path('cards/<int:pk>/delete/', views.card_delete, name='card_delete'),

    #urls pokemon#
    path('pokemons/', views.poke_list, name='poke_list'),
    path('pokemons/<int:pk>/', views.poke_detail, name='poke_detail'),
    path('pokemons/add/', views.poke_add, name='poke_add'),
    path('pokemon/<int:pk>/edit/', views.poke_edit, name='poke_edit'),
    path('pokemons/<int:pk>/delete/', views.poke_delete, name='poke_delete'),

    #urls expansions#
    path('expansions/', views.expan_list, name='expan_list'),
    path('expansions/<int:pk>/', views.expan_detail, name='expan_detail'),
    path('expansions/add/', views.expan_add, name='expan_add'),
    path('expansions/<int:pk>/edit/', views.expan_edit, name='expan_edit'),
    path('expansions/<int:pk>/delete/', views.expan_delete, name='expan_delete'),

    #urls elements#
    path('elements/', views.element_list, name='element_list'),
    path('elements/<int:pk>/', views.element_detail, name='element_detail'),
    path('elements/add/', views.element_add, name='element_add'),  
    path('elements/<int:pk>/edit/', views.element_edit, name='element_edit'),
    path('elements/<int:pk>/delete/', views.element_delete, name='element_delete')

]
