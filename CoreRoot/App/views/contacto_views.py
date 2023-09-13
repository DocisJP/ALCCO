from App.forms import ContactoForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings



def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            subject = f"Mensaje de {name}"
            message = f"De: {name}\nCorreo electrónico: {email}\n\nMensaje:\n{message}"
            
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['orgemail@example.com'])
            
            return redirect('success')  # Redirect to a new page
    else:
        form = ContactoForm()

    return render(request, 'Contacto/contacto.html', {'form': form})

def success(request):
    return render(request, 'Contacto/success.html')