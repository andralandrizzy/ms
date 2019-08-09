from django.shortcuts import render, redirect
from . models import About_us, Timelines, Team, Client, Quote
from portfolio.models import Portfolio
from accounts.models import Testimonial
from services.models import Service
from django.contrib import messages


# Create your views here.


def index(request):
    about_us = About_us.objects.all()[:1]
    services = Service.objects.all()[:3]
    clients = Client.objects.all()[:4]
    portfolios = Portfolio.objects.all()[:8]
    testimonials = Testimonial.objects.order_by('-date_create')
    context = {
        'about_us': about_us,
        'services': services,
        'clients': clients,
        'portfolios': portfolios,
        'testimonials': testimonials,
    }
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']

        quotes = Quote(name=name, email=email, message=message)

        quotes.save()

        messages.success(
            request, 'Quotes have been submitted, We will get back to you soon')
    return render(request, 'pages/index.html', context)


def about(request):
    about_us = About_us.objects.all()[:1]
    timelines = Timelines.objects.all()
    teams = Team.objects.all()
    clients = Client.objects.all()[:4]
    testimonials = Testimonial.objects.order_by('-date_create')
    context = {
        'about_us': about_us,
        'timelines': timelines,
        'teams': teams,
        'clients': clients,
        'testimonials': testimonials,
    }
    return render(request, 'pages/about.html', context)
