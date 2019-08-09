from django.urls import path
from . import views

urlpatterns = [
    path('service', views.services,  name='services'),
    # path('<int:', views.about, name="about")
]
