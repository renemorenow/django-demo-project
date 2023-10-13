from django.urls import path
from . import views

urlpatterns = [
    path('', views.Registro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', views.cerrar_sesion, name="cerrar_sesion"),
    path('login', views.login_user, name="login"),
    # path('contacto/<int:contacto_id>/', views.contacto, name="contacto"),
]
