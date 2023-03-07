from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),

    # authentication
    path('register', views.register),
    path('login', views.login),

    # All Real Estate
    path('get_real_estates', views.get_real_estates),

    # user interaction
    path('adding_real_estate', views.adding_real_estate),
    path('my_real_estates', views.my_real_estates),
    path('delete_my_estate', views.delete_my_estate),

    # Filters
    path('filters_values', views.filters_values),
    path('default_filtered_estate', views.default_filtered_estate),
    path('type_filtered_estate', views.type_filtered_estate),
    path('state_filtered_estate', views.state_filtered_estate),
    path('city_filtered_estate', views.city_filtered_estate),
    path('city_state_price', views.city_state_price),


    # Admin interaction
    path('accept_estate', views.accept_real_estate),
    path('reject_estate', views.reject_real_estate),

]
