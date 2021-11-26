from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('patients/', views.patients_index, name='patients_index'),
    path('patients/create/', views.PatientCreate.as_view(), name='patients_create'),
    path('accounts/signup/', views.signup, name='signup'),
]
