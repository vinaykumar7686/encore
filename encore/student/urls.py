from django.urls import path

from . import views
from .views import register_student, register_student_success, register_for_event

urlpatterns = [
    path('register_for_event/', register_for_event, name='register_for_event'),
    path('student/register/', register_student, name='register_student'),
    path('success', register_student_success, name='registration_success'),
    path("students", views.student_detail),
    path("referrals/<referral_code>/students", views.get_students_basis_referral_code),
    path("registrations/<user_name>", views.registration_detail),
    path("", views.home)
]
