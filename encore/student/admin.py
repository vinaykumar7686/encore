from django.contrib import admin
from .models import Student, Event, Registration

# Register your models here.

admin.site.register(Student)
admin.site.register(Event)
admin.site.register(Registration)
