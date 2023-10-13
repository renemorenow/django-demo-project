from django.urls import path
from . import views
from django.conf import settings #para importar variables del settings
from django.conf.urls.static import static # para agregar rutas y poder mostrar las imagenes o multimedia

urlpatterns = [
    path('', views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)