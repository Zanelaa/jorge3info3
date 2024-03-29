from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Autor, Editora, Livro
from core.serializers import (
    CategoriaSerializer,
    AutorSerializer,
    EditoraSerializer,
    LivroSerializer,
    LivroDetailSerializer,
)


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LivroDetailSerializer
        return LivroSerializer
