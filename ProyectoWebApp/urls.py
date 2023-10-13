from django.urls import path
from ProyectoWebApp import views
from django.conf import settings #para importar variables del settings
from django.conf.urls.static import static # para agregar rutas y poder mostrar las imagenes o multimedia

urlpatterns = [
    path('', views.home, name="Home"),
    # path('servicio', views.servicio, name="Servicio"),
    # path('tienda', views.tienda, name="Tienda"),
    # path('blog', views.blog, name="Blog"),
    # path('contacto', views.contacto, name="Contacto"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)