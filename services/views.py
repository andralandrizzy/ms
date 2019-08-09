from django.shortcuts import render
from . models import Service
from pages.models import Client
from accounts.models import Testimonial
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def services(request):
    services = Service.objects.all()
    paginator = Paginator(services, 3)
    page = request.GET.get('page')
    service_pages = paginator.get_page(page)
    clients = Client.objects.all()
    testimonials = Testimonial.objects.order_by('-date_create')

    context = {
        'services': service_pages,
        'clients': clients,
        # 'testimonials': testimonials
    }
    return render(request,  'services/service.html', context)
