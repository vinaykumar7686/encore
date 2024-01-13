# your_app/forms.py
from django import forms
from .models import Student
from .models import Registration


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['user_name', 'eventId']
