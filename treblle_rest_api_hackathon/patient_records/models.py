from django.db import models

from django.contrib.auth import get_user_model

from django.utils import timezone

from django.core.validators import RegexValidator

import uuid

from tabnanny import verbose 

# Create your models here.

User = get_user_model()

class Drugs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    manufactured_date = models.DateField(default=timezone.now)
    expiration_date = models.DateField(default = timezone.now)
    # patient_prescribed_to = models.ForeignKey(Patient.patient_full_name, verbose_name=_(""), on_delete=models.CASCADE)
    # doctor_prescribed_by = models.ForeignKey(Doctors)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta():
        verbose_name_plural = "Drugs"
    

class Doctors(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    GENDER = [("male", "Male"), ("female", "Female")]
    mobile_number_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    next_of_kin = models.CharField(max_length = 200)
    email = models.EmailField()
    phone_number = models.CharField(
        validators=[mobile_number_regex], max_length=13, blank=True
    )
    gender = models.CharField(max_length=10, choices=GENDER, default="male")
    employment_date = models.DateField(default=timezone.now)
    employment_id  = models.CharField(max_length=6, default=uuid.uuid4)
    specialization = models.CharField(max_length=250)
    # patient_treated = models.ForeignKey(Patient, verbose_name="Patients Treated", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        verbose_name_plural = "Doctors"
        
    def __str__(self) -> str:
        return f'{self.first_name}{self.last_name}'
    
    
class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    GENDER = [("male", "Male"), ("female", "Female")]
    
    mobile_number_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    
    patient_card_number = models.CharField(max_length=8, default=uuid.uuid4)
    patient_full_name = models.CharField(max_length=250)
    patient_address = models.TextField(max_length=250)
    patient_email = models.EmailField()
    next_of_kin = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER, default="male")
    date_of_birth = models.DateField(default=timezone.now)
    date_of_admission = models.DateField(default=timezone.now)
    discharge_date = models.DateField(default = timezone.now)
    patient_mobile_number = models.CharField(
        validators=[mobile_number_regex], max_length=13, blank=True
    )
    next_of_kin_mobile_number = models.CharField(
        validators=[mobile_number_regex], max_length=13, blank=True
    )
    doctor_name = models.ForeignKey(Doctors, verbose_name=" Attending Doctor's Name", on_delete=models.CASCADE)
    doctor_report = models.TextField(max_length=300)
    doctor_report_file_upload = models.FileField(blank=False, null=False, upload_to="upload/patient's files")
    diagnosis = models.TextField(max_length=250)
    # drugs_prescribed = models.TextField(max_length=200)
    drugs_prescribed = models.ForeignKey(Drugs, verbose_name="Drug Prescribed", on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_created=True)
    modified  = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        verbose_name_plural = "Patients"
        
    def __str__(self) -> str:
        return f'{self.patient_full_name }|{ self.patient_card_number}'



class Nurses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    GENDER = [("male", "Male"), ("female", "Female")]
    mobile_number_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    next_of_kin = models.CharField(max_length = 200)
    email = models.EmailField()
    phone_number = models.CharField(
        validators=[mobile_number_regex], max_length=13, blank=True
    )
    gender = models.CharField(max_length=10, choices=GENDER, default="female")
    employment_date = models.DateField(default=timezone.now)
    employment_id  = models.CharField(max_length=6, default=uuid.uuid4)
    specialization = models.CharField(max_length=250)
    patient_attended_to = models.ForeignKey(Patient, verbose_name="Patients Treated", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        verbose_name_plural = "Nurses"
        
    def __str__(self) -> str:
        return f"Nurse: {self.first_name}"

class Billing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    Patient_name = models.ForeignKey(Patient, verbose_name="Patient Name", on_delete=models.CASCADE)
    doctor_attending = models.ForeignKey(Doctors, verbose_name="Attending Doctor", on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    service_bill = models.CharField(max_length=200)
    amount = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=[("active", "Active"), ("closed", "Closed")],
        default="active",
    )
    
    class Meta():
        verbose_name_plural = "Bills"
        
    def __str__(self) -> str:
        return f'{self.Patient_name}'
