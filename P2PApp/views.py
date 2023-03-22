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
#from django.views.decorators.csrf import csrf_exempt
#Aqui se van a crear las vistas //Retornan una respuesta http.

#Request para realizar peticiones

#HTTP Response Para enviar la respuesta usando el protocolo HTTP.

#Esto es una vista
def welcome(request):
	return HttpResponse("<p style='color: red;'>Bienvenido<p>")
def categoriaEdad(request,edad):
	if edad>=18:
		if edad>=60:
			categoria="Tercera Edad"
		else:
			categoria="Adultez"
	else:
		categoria="Infante/Adolescente"
	resultado="<h1>Categoria de la Edad: %s</h1>" %categoria
	return HttpResponse(resultado)

def home(request):
	return render(request,'home.html')

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



def guardar_json(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        with open('data/user', 'w') as f:
            json.dump(data,f)
	    #return render(request,'home.html')
        return HttpResponse(status=200)
		#return redirect('home.html')
		
    else:
        return HttpResponse(status=400)
    
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

def reg_course(request): #Ventana en donde se va a crear el curso
	if request.method=='POST':
		data=json.loads(request.body.decode('utf-8'))
		nombre_archivo= str(uuid.uuid4())+'.json'
		ruta_archivo = os.path.join('data/courses/', nombre_archivo)
		with open(ruta_archivo,'w') as f:
			json.dump(data,f)
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
	print(datos)
	return render(request, 'home.html', {'datos': datos})

	