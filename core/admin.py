from django.contrib import admin

from core.models import Categoria,Editora,Autor,Livro

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)