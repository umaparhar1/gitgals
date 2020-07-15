from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.home, name='converter-home'),
    path('aboutCreators.html', views.creators, name='converter-creators'),
    path('ourPortfolio.html', views.portfolio, name='converter-portfolio'),
    path('converter.html', views.converter, name='converter-app'),
<<<<<<< HEAD
    path('workout.html', views.workout, name='workout-app'),
    path('bmi.html', views.bmi, name='bmi-app'),
    path('caloriesBurned.html', views.caloriesBurned, name='caloriesBurned-app'),
=======
    path('workout.html', views.workout, name = 'workout-app'),
    path('bmi.html', views.bmi, name = 'bmi-app')
>>>>>>> b6bded5ebdf06d592e3275b711dbf7f7b1869cc7
]