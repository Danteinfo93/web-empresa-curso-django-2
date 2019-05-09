from django.contrib import admin
from .models import Link

# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None): # si en tiempo de ejec detectamos q el usuario forma parte del group Personal se le cambian los campos de L/E
        if request.user.groups.filter(name="Personal").exists():
            return ('created', 'updated', 'key', 'name')
        else:
            return ('created', 'updated')

admin.site.register(Link, LinkAdmin)    