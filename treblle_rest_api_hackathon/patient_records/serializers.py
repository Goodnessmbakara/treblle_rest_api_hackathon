from rest_framework import serializers


from patient_records.models import *


class DrugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drugs
        fields  = ['name', 'manufactured_date','expiration_date']
        

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        
class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurses
        fields = '__all__'

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'