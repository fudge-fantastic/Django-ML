from django.shortcuts import render, HttpResponse
import joblib
import numpy as np  # Add this import for array manipulation

model_path = 'static/rfc_model'
model = joblib.load(model_path)
print(f"Model loaded successfully from: {model_path}")


def Home(request):
    return render(request, 'index2.html')

def Prediction(request):
    if request.method == 'POST':
        age = int(request.POST.get('age'))  
        gender = int(request.POST.get('gender', 0))
        hypertension = int(request.POST.get('hypertension',0))
        heart_disease = int(request.POST.get('heart-disease',0))
        smoking_history = int(request.POST.get('smoking-history',0))
        bmi = float(request.POST.get('bmi'))  
        hba1c_level = float(request.POST.get('hba1c-level'))
        blood_glucose_level = int(request.POST.get('blood-glucose-level',0))

        prediction_result = model.predict([[age, gender, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level]])
        output = {"output" : prediction_result}
        print(output)
        return render(request, 'Prediction.html', output)
    else:
        return render(request, 'Prediction.html')

def About(request):
    return render(request, 'About.html')

def Contact(request):
    return render(request, 'Contact.html')


