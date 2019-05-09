from django.db import models

# Create your models here.

#pd: con el verbose indicamos al panel admin como presentar a cada campo
#pd: con upload_to (campo image), indicamos en que carpeta de /media/ debe ir guardando los archivos media
#para hacer esto, se tuvo que crear una carpeta media nueva, y hacer unos cambios en settings.py(ln 124)
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizacion")
   

    #para indicar al panel admin como llamar a la clase y darle un orden a sus instancias
    class Meta: 
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"]

    #para indicar al panel admin como presentar a las instancias de la clase
    def __str__(self):     
        return self.title    