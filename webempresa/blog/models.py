from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User 

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizacion")
   

    #para indicar al panel admin como llamar a la clase y darle un orden a sus instancias
    class Meta: 
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["-created"]

    #para indicar al panel admin como presentar a las instancias de la clase
    def __str__(self):     
        return self.name    

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicacion", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts") # related_name usado para obtener posts desde una categoria en category.html
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizacion")

    #para indicar al panel admin como llamar a la clase y darle un orden a sus instancias
    class Meta: 
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"]

    #para indicar al panel admin como presentar a las instancias de la clase
    def __str__(self):     
        return self.title   