from django.urls import path
from . import views

urlpatterns = [
    path('mysite.html', views.home, name='converter-home'),
    path('aboutCreators.html', views.creators, name='converter-creators'),
    path('ourPortfolio.html', views.portfolio, name='converter-portfolio'),
    path('converter.html', views.converter, name='converter-app')
]