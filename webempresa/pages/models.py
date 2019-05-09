from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Page(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    #para indicar al panel admin como llamar a la clase y darle un orden a sus instancias
    class Meta: 
        verbose_name = "pagina"
        verbose_name_plural = "paginas"
        ordering = ["order"]

    #para indicar al panel admin como presentar a las instancias de la clase
    def __str__(self):     
        return self.title    