from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet, AutorViewSet, EditoraViewSet, LivroViewSet

router = DefaultRouter()
router.register(r"Categorias", CategoriaViewSet)
router.register(r"Autores", AutorViewSet)
router.register(r"Editoras", EditoraViewSet)
router.register(r"Livros", LivroViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
