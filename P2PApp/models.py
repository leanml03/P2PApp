import os
import json

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
def load_courses():
    datos = {}
    ruta_datos = os.path.join(BASE_DIR, 'data/courses')
    for archivo in os.listdir(ruta_datos):
        if archivo.endswith('.json'):
            with open(os.path.join(ruta_datos, archivo)) as f:
                datos[archivo[:-5]] = json.load(f)
    return datos

