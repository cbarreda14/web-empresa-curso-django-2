from django.contrib import admin
from .models import category, post

# Register your models here.
#esto sirve para registrar en el panel del admin, osea que aparezca en el admin
class categoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class postAdmin(admin.ModelAdmin):
    #que campos adicionales se van a mostrar
    readonly_fields = ('created','updated')
    #mostrar columnas adicionales a al grilla de la lista
    list_display = ('title','author','published','post_categories')
    #mostrar en que orden quiere que se realize en la grilla
    ordering = ('author',)
    #campos de busqueda /cuando se busca una tabla foreing se tiene que colocar el nombredel modelo__nombrecampo
    search_fields = ('title','content','author__username','categories__name')
    #jerarquia de fechas en la grilla
    date_hierarchy = 'published'
    #es para el filtro que te aparece al costado
    list_filter = ('title','author__username','categories__name')

    def post_categories(self,obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"

admin.site.register(category,categoryAdmin)
admin.site.register(post,postAdmin)