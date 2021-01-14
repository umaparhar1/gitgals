from django.shortcuts import render
from django.http import HttpResponse
import yfinance as yf

# Create your views here.


def home(request):
    return render(request, 'converter/index.html', {})


def creators(request):
    return render(request, 'converter/aboutCreators.html', {})


def portfolio(request):
    return render(request, 'converter/ourPortfolio.html', {})


def converter(request):
    return render(request, 'converter/converter.html', {})


def workout(request):
    return render(request, 'converter/workout.html', {})


def bmi(request):
    return render(request, 'converter/bmi.html', {})


def caloriesBurned(request):
    return render(request, 'converter/caloriesBurned.html', {})


def workoutIdeas(request):
    return render(request, 'converter/workoutIdeas.html', {})

def tutoring(request):
    return render(request, 'converter/tutoring.html', {})

def stock(request):
    return render(request, 'converter/stock.html', {})

def studentPage(request):
    return render(request, 'converter/studentPage.html', {})

def tutorPage(request):
    return render(request, 'converter/tutorPage.html', {})
