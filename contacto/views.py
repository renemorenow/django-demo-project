from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .forms import FormularioContacto

# Create your views here.

def contacto(request):
    miFormulario = FormularioContacto()
    if request.method=="POST":
        miFormulario = FormularioContacto(data=request.POST)
        if miFormulario.is_valid():
            # data_form = miFormulario.cleaned_data
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            email_from = settings.EMAIL_HOST_USER
            send_mail("Mensaje django", contenido, email_from, [email],)
            #
            email_send = EmailMessage(subject="Mensaje django", body=contenido, from_email=email_from, to=email_from, reply_to=email)
            email_send.send()
            #
            return redirect("/contacto/?valido")
    
    return render(request, "contacto.html", {"frmContacto":miFormulario})