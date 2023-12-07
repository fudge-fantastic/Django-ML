from django.urls import path
from home import views

urlpatterns = [
    path('', views.Home, name='home'),
    # From home, we have views files, and in that file, we're importing a function which we wrote 
    path('prediction', views.Prediction, name='prediction'),
    path('about', views.About, name='about')
]