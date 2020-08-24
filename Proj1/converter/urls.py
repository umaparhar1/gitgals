from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.home, name='converter-home'),
    path('aboutCreators.html', views.creators, name='converter-creators'),
    path('ourPortfolio.html', views.portfolio, name='converter-portfolio'),
    path('converter.html', views.converter, name='converter-app'),
    path('workout.html', views.workout, name='workout-app'),
    path('bmi.html', views.bmi, name='bmi-app'),
    path('caloriesBurned.html', views.caloriesBurned, name='caloriesBurned-app'),
    path('workoutIdeas.html', views.workoutIdeas, name='workoutIdeas-app'),
    path('stock.html', views.stock, name='stock-app'),
]