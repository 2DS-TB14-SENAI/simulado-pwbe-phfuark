from django.shortcuts import render
from .models import Livro

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})