from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'converter/mysite.html', {})

def creators(request):
    return render(request, 'converter/aboutCreators.html', {})

def portfolio(request):
    return render(request, 'converter/ourPortfolio.html', {})