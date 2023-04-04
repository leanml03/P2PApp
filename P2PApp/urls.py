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
    path('registrar/guardar-json/',guardar_json,name='guardar-json'),
    path('home/',home, name='home'),
    path('welcome/',welcome),
    path('home/crear_curso/',crear_curso,name='crear_curso'),
    path('home/crear_curso/reg_curso/',reg_curso,name='reg_curso'),
    path('home/sincronizar_datos/',sincronizar_datos,name='sincronizar_datos'),
    path('acceso/',acceso,name='acceso'),
    path('invalido/',datos_invalidos,name='invalido'),
    path('acceso/cargado/',acceso_cargado,name='accesocargado'),
    path('exportar_usuario/',exportar_usuario,name='exportar_usuario'),
    path('exportar_curso/',exportar_curso,name='exportar_curso'),
    path('crear_foro/reg_foro/',reg_foro,name='reg_foro'),
    path('curso/',curso,name='curso'),
    path('curso/crear_foro/',crear_foro,name='crear_foro'),
    path('registrar/', registrar, name='registrar'), 
    path('welcome/', welcome, name='welcome')
]
