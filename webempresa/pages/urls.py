from django.urls import path
from . import views

urlpatterns = [
    #paths page
    path('<int:page_id>/<slug:page_slug>', views.page, name="page"), # aca se ve como agarramos category_id de manera dinamica la convertimos a int y la pasamos a su views como parametro
]