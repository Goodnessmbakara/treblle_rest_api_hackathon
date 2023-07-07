from django.shortcuts import render

from django.http import JsonResponse, HttpResponse

from rest_framework import status, generics, permissions

from rest_framework.decorators import api_view

from rest_framework.response import Response

from patient_records.serializers import *

# Create your views here.

@api_view(['Get'])
def get_all_patient(request, format= None):
    
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return JsonResponse({"patients":serializer.data})
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT','DELETE'])
def get_patient_details(request, id, format=None):
    try:
        patient = Patient.objects.get(pk=id)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['Get'])
def get_all_doctors(request, format= None):
    if request.method == 'GET':
        doctors = Doctors.objects.all()
        serializer = DoctorsSerializer(doctors, many=True)
        return JsonResponse({"doctors":serializer.data})
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get', 'PUT','DELETE'])
def get_doctor_details(request, id, format=None):
    try:
        doctor = Doctors.objects.get(pk=id)
    except Doctors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = DoctorsSerializer(doctor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DoctorsSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['Get'])
def get_all_nurses(request, format= None):
    if request.method == 'GET':
        nurses = Nurses.objects.all()
        serializer = NurseSerializer(nurses, many=True)
        return JsonResponse({"nurses":serializer.data})
           
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get', 'PUT','DELETE'])
def get_nurse_details(request, id, format=None):
    try:
        nurse = Nurses.objects.get(pk=id)
    except Nurses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = NurseSerializer(nurse)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = NurseSerializer(nurse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        nurse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['Get', 'POST'])
def get_all_drugs(request, format= None):
    if request.method == 'GET':
        nurses = Drugs.objects.all()
        serializer = DrugsSerializer(nurses, many=True)
        return JsonResponse({"drugs":serializer.data})
    
    elif request.method == 'POST':
        serializer = DrugsSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get', 'PUT','DELETE'])
def get_drug_details(request, id, format=None):
    try:
        drug = Drugs.objects.get(pk=id)
    except Drugs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = DrugsSerializer(drug)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrugsSerializer(drug, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)