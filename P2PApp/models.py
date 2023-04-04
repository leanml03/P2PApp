import os
import json
import shutil
from P2PApp.settings import BASE_DIR

#Carga de los datos json
def cargar_datos_json():
    datos = {}
    ruta_datos = os.path.join(BASE_DIR, 'data')
    for archivo in os.listdir(ruta_datos):
        if archivo.endswith('.json'):
            with open(os.path.join(ruta_datos, archivo)) as f:
                datos[archivo[:-5]] = json.load(f)
    return datos


#Carga de los cursos
def cargar_cursos():
    datos = {}
    ruta_datos = os.path.join(BASE_DIR, 'data/cursos')
    for archivo in os.listdir(ruta_datos):
        if archivo.endswith('.json'):
            with open(os.path.join(ruta_datos, archivo)) as f:
                datos[archivo[:-5]] = json.load(f)
    return datos

#Carga del usuario
current_user=None
def cargar_perfil():
    data=os.path.join(BASE_DIR,'data/usuario.json')
    try:
       f=open(data,"r")
    except:
        return
    datos= json.loads(f.read())
    print("Log: Usuario ha sido cargado")
    current_user=datos
    return datos                

def revisar_cursos(name):
    print("entro")
    ruta_datos = os.path.join(BASE_DIR, 'data/cursos')
    for archivo in os.listdir(ruta_datos):
        print(archivo[:-5])
        print(name)
        if archivo.endswith('.json'):
            if archivo[:-5]+".json" == name:
                    return True
    return False

def copiar_archivo_exportado(path,path2):
    src = path #'/path/to/original/file.json'
    dst = path2 #'/path/to/new/location/file.json'
    shutil.copy(src, dst)

