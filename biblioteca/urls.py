from django.contrib import admin
from django.urls import path
from livros.views import listar_livros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livros/', listar_livros, name='listar_livros'),
]