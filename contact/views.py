from django.shortcuts import render, redirect
from django.contrib import messages
from pages.models import Client
from .models import ContactForm, ContactInfo

# Create your views here.


def contact(request):
    clients = Client.objects.all()
    contact_me = ContactInfo.objects.all() 
    context = {
        'clients': clients,
        'contact_me': contact_me

    }
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']

        contact = ContactForm(name = name, email = email, message = message, 
        subject = subject)

        contact.save()
        messages.success(request, 'Your message has been submitted, We will get back to you soon')
    return render(request,  'contact/contact.html', context)






