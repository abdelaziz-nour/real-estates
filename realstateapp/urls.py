from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('register', views.register),
    path('login', views.login),
    path('adding_estate', views.adding_realstate),
    path('defalute_filttered_estate', views.defalute_filttered_estate),
    path('type_filttered_estate', views.type_filttered_estate),
    path('getting_states', views.getting_states),
    path('getting_my_estate', views.getting_my_estate),
    path('city_filttered_estate', views.city_filttered_estate),
    path('state_filttered_estate', views.state_filttered_estate),
    path('city_state_price', views.city_state_price),
    path('delete_my_estate', views.delete_my_estate),
    path('accept_estate', views.accept_estate),
    path('reject_estate', views.reject_estate),
    

]