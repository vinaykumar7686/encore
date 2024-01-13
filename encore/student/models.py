from django.db import models


class Student(models.Model):
    user_name = models.CharField(primary_key=True, max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    full_name = models.CharField(max_length=70)
    collegeName = models.CharField(max_length=100)
    graduationYear = models.IntegerField(default=1, blank=True)
    dob = models.DateField(blank=True)
    phoneNumber = models.CharField(max_length=15, blank=True)
    referralCode = models.CharField(max_length=10, blank=True)
    myReferralCode = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.user_name


class Event(models.Model):
    eventId = models.CharField(primary_key=True, max_length=10)
    eventName = models.CharField(max_length=100)

    def __str__(self):
        return self.eventName


class Registration(models.Model):
    user_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_name)
