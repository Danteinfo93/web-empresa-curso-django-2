from django.urls import path
from . import views

urlpatterns = [
    #paths blog
    path('', views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name="category"), # aca se ve como agarramos category_id de manera dinamica la convertimos a int y la pasamos a su views como parametro
]