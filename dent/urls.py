from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about_us'),
    path('prices/', PricesView.as_view(), name='prices'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('base/', BaseView.as_view(), name='base'),
]

