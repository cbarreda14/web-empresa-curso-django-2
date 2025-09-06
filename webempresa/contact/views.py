from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #enviamos el correo y redireccionamos
            message = EmailMessage(  
                subject="La Caffetiera: Nuevo mensaje de contacto",
                body=f"De: {name} <{email}>\n\nEscribió:\n\n{content}",
                from_email="no-contestar@inbox.maintrap.io",
                to = ["cbarreda221@gmail.com"],
                reply_to=[email]
            )
            try:
                message.send()
                
                return redirect(reverse('contact')+"?ok")
            except:
                #algo no ha ido bien redireccionamos a fail
                return redirect(reverse('contact')+"?fail")
                
    return render(request,'contact/contact.html',{'form':contact_form})