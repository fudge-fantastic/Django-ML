from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):
    return render(request, 'index2.html')

def Prediction(request):
    return render(request, 'Prediction.html')

def About(request):
    return render(request, 'About.html')

