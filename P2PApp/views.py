import os
import uuid
import json
from django.http import HttpResponse
from django.template import Template, Context
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from P2PApp.models import *
from django.template import TemplateDoesNotExist
import hashlib

import shutil
from django.conf import settings



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

import shutil
from django.conf import settings
#from django.views.decorators.csrf import csrf_exempt
#Aqui se van a crear las vistas //Retornan una respuesta http.

#Request para realizar peticiones

#HTTP Response Para enviar la respuesta usando el protocolo HTTP.

#Esto es una vista
def welcome(request):
	return HttpResponse("<p style='color: red;'>Bienvenido<p>")


def home(request):
	user=load_profile
	return render(request,'home.html',{'user':user})

def course(request):
	user=load_profile
	return render(request,'course.html',{'user':user})

def register(request):
	"""openTemplate=open(os.path.abspath("P2PApp/templates/register.html")) #Se llama a la ruta importando OS para poder correrlo en cualquier computador
	template=Template(openTemplate.read()) #Se lee el HTML y se guarda en template (Se usa Template de libreria de django)
	openTemplate.close() #Se cierra la obtencion del template para no dejarlo vulnerable
	context=Context() #Objeto que nos permite indicar cuales objetos y variables va a utilizar la plantilla
	document=template.render(context) ##Se renderiza el contexto
	return HttpResponse(document) ##Se devuelve el html como respuesta"""
	return render(request,'register.html')

def welcome(request):
	"""openTemplate=open(os.path.abspath("P2PApp/templates/welcome.html")) #Se llama a la ruta importando OS para poder correrlo en cualquier computador
	template=Template(openTemplate.read()) #Se lee el HTML y se guarda en template (Se usa Template de libreria de django)
	openTemplate.close() #Se cierra la obtencion del template para no dejarlo vulnerable
	context=Context() #Objeto que nos permite indicar cuales objetos y variables va a utilizar la plantilla
	document=template.render(context) ##Se renderiza el contexto
	return HttpResponse(document) ##Se devuelve el html como respuesta"""
	return render(request,'welcome.html')


""""
def guardar_json(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        with open('data/user', 'w') as f:
            json.dump(data,f)
	    #return render(request,'home.html')
        return HttpResponse(status=200)
		#return redirect('home.html')
		
    else:
        return HttpResponse(status=400)"""
    
def guardar_json(request):
	if request.method=='POST':
		data=json.loads(request.body.decode('utf-8'))
		with open('data/user.json','w') as f:
			json.dump(data,f)
		return HttpResponseRedirect('/home/')
	else:
		return HttpResponse(status=400)
def create_course(request): #Ventana en donde se va a crear el curso
	return render(request,'crear_curso.html')


#Se crea un curso con Hash ID
def reg_course(request): #Ventana en donde se va a crear el curso
	if request.method=='POST':
		data=json.loads(request.body.decode('utf-8'))
		datax=json.dumps(data,sort_keys=True)
		hash_object=hashlib.sha256(datax.encode())
		nombre_archivo= hash_object.hexdigest()+'.json'
		ruta_archivo = os.path.join('data/courses/', nombre_archivo)
		if(check_courses(nombre_archivo)):
			print("Log: No se puede registrar el curso, ya se encuentra registrado.")
			return redirect('invalid')
			
		else:
			with open(ruta_archivo,'w') as f:
				json.dump(data,f)
			print("Log: El curso se ha registrado satisfactoriamente.")
			return HttpResponseRedirect('/home/')

		
	else:
		return HttpResponse(status=400)
	
def create_forum(request): #Ventana en donde se va a crear el foro
	return render(request,'crear_foro.html')

def reg_forum(request): #Ventana en donde se va a crear el foro
	if request.method=='POST':
		data=json.loads(request.body.decode('utf-8'))

		nombre_archivo= settings.UID_ACTUAL + '.json'
		ruta_archivo = os.path.join('data/courses/', nombre_archivo)

		
		with codecs.open(ruta_archivo, 'r',encoding='utf-8') as f:
			json_existente = json.load(f)
	
		json_existente['forums'].append(data)

		with open(ruta_archivo,'w') as f:
			json.dump(json_existente,f)

		return HttpResponseRedirect('/home/')
	else:
		return HttpResponse(status=400)
		
def sync_data(request):
	"""folder_path = "data/courses/"
	file_list = os.listdir(folder_path)
	json_list = []
	for file_name in file_list:
		if file_name.endswith('.json'):
			file_path = os.path.join(folder_path, file_name)
			with open(file_path, 'r') as json_file:
				json_data = json.load(json_file)
				json_list.append(json_data)"""
	datos = load_courses()
	user=load_profile()
	print(datos)
	return render(request, 'home.html', {'datos': datos,'user':user})
def login(request):
	datos=load_profile()
	return render(request,'login.html',{'datos':datos})

def InvalidData(request):
	if(request.method=='GET'):
		print("hola")
		return redirect('/home/')

		
	else:
		return render("<div>hola</div>")
	




def loginloaded(request):
    if request.method == 'POST':
        file = request.FILES.get('json_file', None)
        if file:
            # Verificar que el archivo tenga la extensión .json
            if file.name.endswith('.json'):
                # Crear la ruta de destino
                file_path = os.path.join(settings.BASE_DIR, 'data', 'user.json')
                # Copiar el archivo a la ubicación de destino
                with open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Solo se permiten archivos JSON'})
        else:
            return JsonResponse({'success': False, 'error': 'No se proporcionó ningún archivo'})
    else:
        return render(request, 'login.html')
    

def exportUser(request):
	copy_export_file(os.path.join('data/user.json'),os.path.join('export/users/user.json'))
	return render(request,'checkdata.html')

def exportCourse(request):
	return render(request,'checkdata.html')

