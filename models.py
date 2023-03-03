from django.db import models

class Doctor(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    speciality=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Patient(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    contact=models.IntegerField()
    disease=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date1=models.DateField()
    time1=models.TimeField()
    def __str__(self):
        return self.doctor.name+"--"+sedlf.patient.name

# Create your models here.
