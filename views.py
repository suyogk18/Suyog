from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import * 
from django.contrib.auth import authenticate,logout,login
# Create your views here.

def about(request):
    return render(request, 'ab.html')

def services(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def start(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors=Doctor.objects.all()
    patients=Patient.objects.all()
    appointments=Appointment.objects.all()

    doct=0;
    patt=0;
    app=0;
    for i in doctors:
        doct+=1
    for i in patients:
        patt+=1
    for i in appointments:
        app+=1
    new={'doct':doct,'patt':patt,'app':app}
    return render(request, 'start.html',new)

def log(request):
    error=""
    if request.method=="POST":
        a=request.POST['usname']
        b=request.POST['password']
        user=authenticate(username=a,password=b)
        try:
            if user.is_staff:
                login(request,user)
                error="No"
            else:
                error="Yes"
        except:
            error="Yes"
    s={'error':error}
    return render(request, 'log.html',s)

def logout_ad(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    dr = Doctor.objects.all()
    d= {'dr':dr}
    return render(request, 'view_doctor.html',d)

def ad_doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=="POST":
        nm=request.POST['name']
        ct=request.POST['contact']
        sz=request.POST['speciality']
        try:
            Doctor.objects.create(name=nm,contact=ct,speciality=sz)
            error="No"
        except:
            error="Yes"
    t={'error':error}
    return render(request, 'add_doctor.html',t)

def del_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    dc= Doctor.objects.get(id=pid)
    dc.delete()
    return redirect('view_doctor')


def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pt = Patient.objects.all()
    p= {'pt':pt}
    return render(request, 'view_patient.html',p)

def ad_patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=="POST":
        nm=request.POST['name']
        gd=request.POST['gender']
        ct=request.POST['contact']
        add=request.POST['address']
        ds=request.POST['disease']
        try:
            Patient.objects.create(name=nm,gender=gd,contact=ct,address=add,disease=ds)
            error="No"
        except:
            error="Yes"
    t={'error':error}
    return render(request, 'add_patient.html',t)

def del_patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    pat= Patient.objects.get(id=pid)
    pat.delete()
    return redirect('view_patient')

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.all()
    apt= {'appointment':appointment}
    return render(request, 'view_appoint.html',apt)

def ad_appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1=Doctor.objects.all()
    patient1=Patient.objects.all()
    if request.method=="POST":
        dc=request.POST['doctor']
        pa=request.POST['patient']
        d1=request.POST['date']
        t1=request.POST['time']
        doctor=Doctor.objects.filter(name=dc).first()
        patient=Patient.objects.filter(name=pa).first()
        try:
            Appointment.objects.create(doctor=doctor,patient=patient,date1=d1,time1=t1)
            error="No"
        except:
            error="Yes"
    t={'doctor':doctor1,'patient':patient1,'error':error}
    return render(request, 'add_appoint.html',t)

def del_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    aptt= Appointment.objects.get(id=pid)
    aptt.delete()
    return redirect('view_appoint')



