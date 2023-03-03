"""Hospital_Mgmt_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HMS_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('abt/', about, name='About'),
    path('serv/', services, name='service'),
    path('con/', contact, name='contact'),
    path('', start, name='home'),
    path('admin_login/', log, name='login'),
    path('logout/', logout_ad, name='logout'),
    path('view_doctor/', view_doctor, name='view_doctor'),
    path('add_doctor/', ad_doctor, name='add_doctor'),
    path('delete_doctor(?P<int:pid>)/', del_doctor, name='delete_doctor'),
    path('view_patient/', view_patient, name='view_patient'),
    path('add_patient/', ad_patient, name='add_patient'),
    path('delete_patient(?P<int:pid>)/', del_patient, name='delete_patient'),
    path('view_appoint/', view_appointment, name='view_appoint'),
    path('add_appoint/', ad_appointment, name='add_appoint'),
    path('delete_appointment(?P<int:pid>)/', del_appointment, name='delete_appointment'),
]
