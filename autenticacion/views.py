from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Para manejo de mensajes:
from django.contrib import messages


class Registro(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # Hacer login automatico:
            login(request, usuario)
            # Redireccionar al Home:
            return redirect("Home")
        else:
            # Manejo de excepciones:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro/registro.html", {"form": form})


# Create your views here.

def cerrar_sesion(request):
    logout(request)
    return redirect("Home")

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=pwd)
            if usuario:
                login(request, usuario)
                return redirect("Home")
            else:
                messages.error(request, "Usuario o Password invalidos")
        else:
            # Manejo de excepciones:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
    else:
        form = AuthenticationForm()
    return render(request, "login/login.html", {"form": form})