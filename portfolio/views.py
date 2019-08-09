from django.shortcuts import render, get_object_or_404
from pages.models import Client
from . models import Portfolio
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.


def portfolios(request):
    clients = Client.objects.all()
    portfolios = Portfolio.objects.order_by('-date')
    paginator = Paginator(portfolios, 6)
    page = request.GET.get('page')
    paged_portfolios = paginator.get_page(page)
    context = {
        'clients': clients,
        'portfolios': paged_portfolios,
    }
    return render(request, 'portfolio/portfolio.html', context)


def portfolio(request, port_id):
    portfolio = get_object_or_404(Portfolio, pk=port_id)
    clients = Client.objects.all()
    context = {
        'portfolio': portfolio,
        'clients': clients,
    }
    return render(request, 'portfolio/portfolio_details.html', context)
