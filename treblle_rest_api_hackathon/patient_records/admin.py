from django.contrib import admin

from patient_records.models import *

admin.site.site_header = 'Patient Management Webapp'


admin.site.register(Drugs)

admin.site.register(Patient)

admin.site.register(Doctors)

admin.site.register(Nurses)

admin.site.register(Billing)