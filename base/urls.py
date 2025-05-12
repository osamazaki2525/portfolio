from django.urls import path
from . import views

app_name='base'
#   self-driving-Car    AI-Gym-Trainer    face-recognition     Churn-Prediction          Desktop-sales-LINQ     Desktop-sales
urlpatterns = [
	path('', views.home , name='home'),
    path('contact/', views.contact , name='contact'),

    # projects urls

#   - self-driving-Car
    path('self-driving-Car/', views.selfdrivingCar , name='self-driving-Car'),
#   - AI-Gym-Trainer
    path('AI-Gym-Trainer/', views.AIGymTrainer , name='AI-Gym-Trainer'),
#   - face-recognition
    path('face-recognition/', views.facerecognition , name='face-recognition'),
#   - Churn-Prediction
    path('Churn-Prediction/', views.ChurnPrediction , name='Churn-Prediction'),
#   - Desktop-sales-LINQ
    path('Desktop-sales-LINQ/', views.DesktopsalesLINQ , name='Desktop-sales-LINQ'),
#   - Desktop-sales
    path('Desktop-sales/', views.Desktopsales , name='Desktop-sales'),
]