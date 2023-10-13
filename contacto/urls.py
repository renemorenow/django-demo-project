from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto, name="Contacto"),
    # path('contacto/<int:contacto_id>/', views.contacto, name="contacto"),
]
