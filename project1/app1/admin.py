from django.contrib import admin
from . models import Student ,Consultation
from .models import Booking

# Register your models here.
admin.site.register(Student)
admin.site.register(Consultation)
admin.site.register(Booking)