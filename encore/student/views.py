# from django.http import Http404
from django.shortcuts import render
from .models import Registration, Event, Student
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from .forms import EventRegistrationForm


def home(request):
    return render(request, "index.html")


def student_detail(request):
    s_info = Student.objects.all()
    return render(request, "view_students.html", {"students": s_info})


def registration_detail(request, user_name):
    r_info = Registration.objects.filter(user_name=user_name)
    return render(request, "view_reg.html", {"registrations": r_info})


def event_detail(request, student_email):
    s_info = Event.objects.all()
    return render(request, "polls/detail.html", {"poll": s_info})


def get_students_basis_referral_code(request, referral_code):
    students_basis_referral = Student.objects.filter(referralCode=referral_code)
    print(students_basis_referral)
    return render(request, "students_basis_referral.html", {"registrations": students_basis_referral})


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # You can define a success page or redirect as needed
    else:
        form = StudentRegistrationForm()

    return render(request, 'student_registration_form.html', {'form': form})


def register_student_success(request):
    return render(request, 'registration_success.html')


def register_for_event(request):
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # Redirect to a success page or adjust as needed
    else:
        form = EventRegistrationForm()

    return render(request, 'event_registration_form.html', {'form': form})