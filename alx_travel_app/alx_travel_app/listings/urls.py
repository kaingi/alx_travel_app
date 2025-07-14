# alx_travel_app/alx_travel_app/listings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sample_view),
]
