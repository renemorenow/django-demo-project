from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.

def blog(request):
    post_all = Post.objects.all()
    return render(request, "blog.html", {"posts":post_all})
    

def categoria(request, categoria_id):
    categoria_filter = Categoria.objects.get(id=categoria_id)
    post_categoria = Post.objects.filter(categorias=categoria_filter)
    return render(request, "categorias.html", {"categoria":categoria_filter, "posts":post_categoria})
    