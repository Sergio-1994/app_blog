from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria


class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    resource_class = CategoriaResource
    list_display = [
        'id', 
        'nombre', 
        'fecha_creacion',
        'estado'
    ]

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellidos', 'correo']
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

<<<<<<< HEAD
class PostAdmin(admin.ModelAdmin):
    search_fields =['titulo']
    list_display = [
        'id', 
        'titulo',
        'slug', 
        'descripcion',
        'estado',
        'fecha_creacion',
        'categoria',
        'autor'
    ]
    

=======
>>>>>>> parent of 2354e31 (Añadido modelo Post, y modulo ckeditor)
admin.site.register(Categoria,CategoriaAdmin) 
admin.site.register(Autor, AutorAdmin)
