from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def home(request):
	return render(request, 'base/home.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(
                f"New Contact: {subject}",
                f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                'ahmdmadbdallhmhmd@gmail.com',  # email that send mails
                ['osamazaki2525@gmail.com'],  # my receiver email that receive mails
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('base:contact')
    else:
        form = ContactForm()
    return render(request, 'base/contact.html', {'form': form})


##############################################################################################
#   self-driving-Car    AI-Gym-Trainer    face-recognition     Churn-Prediction          Desktop-sales-LINQ     Desktop-sales


#   -  self-driving-Car
def  selfdrivingCar(request):
	return render(request, 'base/self-driving-Car.html')

#   - AI-Gym-Trainer
def AIGymTrainer(request):
	return render(request, 'base/AI-Gym-Trainer.html')

#   - face-recognition
def facerecognition(request):
	return render(request, 'base/face-recognition.html')

#   - Churn-Prediction 
def ChurnPrediction (request):
	return render(request, 'base/Churn-Prediction.html')

#   - Desktop-sales-LINQ
def DesktopsalesLINQ(request):
	return render(request, 'base/Desktop-sales-LINQ.html')

#   - Desktop-sales
def Desktopsales(request):
	return render(request, 'base/Desktop-sales.html')




