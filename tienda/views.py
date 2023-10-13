from django.shortcuts import render
from .models import CategoriaProducto, Producto

# Create your views here.

def tienda(request):
    producto_all = Producto.objects.all()
    return render(request, "tienda/tienda.html", {"productos":producto_all})
    

def categoria(request, categoria_id):
    categoria_filter = Categoria.objects.get(id=categoria_id)
    post_categoria = Post.objects.filter(categorias=categoria_filter)
    return render(request, "categorias.html", {"categoria":categoria_filter, "posts":post_categoria})
