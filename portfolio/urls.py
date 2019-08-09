from django.urls import path
from . import views

urlpatterns = [
    path('portfolios', views.portfolios,  name='portfolios'),
    path('portfolio/<int:port_id>', views.portfolio, name='portfolio'),
]
