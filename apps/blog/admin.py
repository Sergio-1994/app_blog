from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

#Nota: al momento de usar import/export debemos crear esta clase 
class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    resource_class = CategoriaResource
    list_display = [
        'id', 
        'nombre', 
        'fecha_creacion',
        'estado'
    ]

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre', 'apellidos', 'correo']
    resource_class = AutorResource
    list_display = [
        'id', 
        'nombre', 
        'apellidos', 
        'facebook', 
        'twitter', 
        'instagram', 
        'web',
        'correo', 
        'fecha_creacion', 
        'estado'

    ]

class PostAdmin(admin.ModelAdmin):
    search_fields =['titulo']
    list_display = [
        'id', 
        'titulo',
        'slug', 
        'descripcion',
        'contenido',
        'imagen',
        'estado',
        'fecha_creacion',
        'categoria',
        'autor'
    ]
    

admin.site.register(Categoria,CategoriaAdmin) 
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)
