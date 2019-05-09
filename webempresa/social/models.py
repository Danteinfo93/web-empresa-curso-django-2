from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre Clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red Social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    #para indicar al panel admin como llamar a la clase y darle un orden a sus instancias
    class Meta: 
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ["name"]

    #para indicar al panel admin como presentar a las instancias de la clase
    def __str__(self):     
        return self.name    