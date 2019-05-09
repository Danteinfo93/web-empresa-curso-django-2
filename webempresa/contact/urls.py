from django.urls import path
from . import views

urlpatterns = [
    #paths contact
    path('', views.contact, name="contact"),
    
]