import json
import os
from todo.modelo import Tarea


class SerializadorJSON:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.crear_directorio_si_no_existe()

    def crear_directorio_si_no_existe(self):
        directorio = os.path.dirname(self.ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)

    def guardar(self, tareas):
        datos = [t.a_diccionario() for t in tareas]
        with open(self.ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def cargar(self):
        if not os.path.exists(self.ruta_archivo):
            return []
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                return [Tarea.desde_diccionario(d) for d in datos]
        except json.JSONDecodeError:
            return []
