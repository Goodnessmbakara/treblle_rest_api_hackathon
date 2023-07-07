from django.urls import path

from . import views

# from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('get-patients/', views.get_all_patient, name='get_all_patient'),
    path('get-patient/<int:id>', views.get_patient_details, name='get_patient_details'),
    path('get-doctors/', views.get_all_doctors, name='get_all_doctors'),
    path('get-doctor/<int:id>', views.get_doctor_details, name='get_doctor_details'),
    path('get-nurses/', views.get_all_nurses, name='get_all_nurses'),
    path('get-nurse/<int:id>', views.get_nurse_details, name='get_nurse_details'),
    path('get-drugs/', views.get_all_drugs, name='get_all_drugs'),
    path('get-drug/<int:id>', views.get_drug_details, name='get_drug_details'),
    
]

# urlpatterns = format_suffix_patterns(urlpatterns)