from django.contrib import admin
from .models import Service

# Register your models here.

#clase para exterder la funcionalidad del panel admin
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields =  ('created', 'updated')
#redefinimos el campo, para indicar q campos del modelo son solo de lectura.
#pd: created y updated eran capos de un tipo oculto en el panel admin por defecto para django 
#ahora si van a aparecer en el panel pero solo como campos de lectura  

#para que aparezca el modelo en el panel admin
admin.site.register(Service, ServiceAdmin)