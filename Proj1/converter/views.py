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
<<<<<<< HEAD
    return render(request, 'converter/bmi.html', {})

def caloriesBurned(request):
    return render(request, 'converter/caloriesBurned.html', {})
=======
    return render(request, 'converter/bmi.html', {})
>>>>>>> b6bded5ebdf06d592e3275b711dbf7f7b1869cc7
