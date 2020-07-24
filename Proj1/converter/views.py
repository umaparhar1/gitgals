from django.shortcuts import render
from django.http import HttpResponse

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
