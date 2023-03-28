"""P2PApp URL Configuration

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
from P2PApp.views import *
from django.contrib import admin
from django.urls import path




urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register),
    path('register/guardar-json/',guardar_json,name='guardar-json'),
    path('home/',home, name='home'),
    path('welcome/',welcome),
    path('create_course/',create_course,name='create_course'),
    path('create_course/reg_course/',reg_course,name='reg_course'),
    path('home/sync_data/',sync_data,name='sync_data'),
    path('login/',login,name='login'),
    path('invalid/',InvalidData,name='invalid'),
    path('login/loaded/',loginloaded,name='loginloaded'),
    path('exportUser/',exportUser,name='exportUser'),
    path('exportCourse/',exportCourse,name='exportCourse')
]
