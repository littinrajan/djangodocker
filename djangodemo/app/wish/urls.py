from django.urls import path
from . import views

urlpatterns = [
    path('wishme', views.wishme, name="wishme"),
    path('funfact', views.funfact, name="funfacts"),
    path('helloworld', views.helloworld, name="funfacts"),
]
