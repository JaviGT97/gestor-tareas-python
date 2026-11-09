import uuid
from datetime import datetime
from enum import Enum


class Prioridad(Enum):
    BAJA = "baja"
    MEDIA = "media"
    ALTA = "alta"


class Tarea:
    def __init__(self, titulo, descripcion="", fecha_limite=None, prioridad=Prioridad.MEDIA.value, etiquetas=None):
        self.id = str(uuid.uuid4())
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_creacion = datetime.now().isoformat()
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad
        self.etiquetas = etiquetas if etiquetas else []
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def desmarcar(self):
        self.completada = False

    def editar(self, titulo=None, descripcion=None, fecha_limite=None, prioridad=None, etiquetas=None):
        if titulo:
            self.titulo = titulo
        if descripcion is not None:
            self.descripcion = descripcion
        if fecha_limite is not None:
            self.fecha_limite = fecha_limite
        if prioridad:
            self.prioridad = prioridad
        if etiquetas is not None:
            self.etiquetas = etiquetas

    def a_diccionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "fecha_creacion": self.fecha_creacion,
            "fecha_limite": self.fecha_limite,
            "prioridad": self.prioridad,
            "etiquetas": self.etiquetas,
            "completada": self.completada
        }

    @classmethod
    def desde_diccionario(cls, datos):
        tarea = cls(
            datos.get("titulo", ""),
            datos.get("descripcion", ""),
            datos.get("fecha_limite"),
            datos.get("prioridad", Prioridad.MEDIA.value),
            datos.get("etiquetas", [])
        )
        tarea.id = datos.get("id", str(uuid.uuid4()))
        tarea.fecha_creacion = datos.get(
            "fecha_creacion", datetime.now().isoformat())
        tarea.completada = datos.get("completada", False)
        return tarea


class GestorTareas:
    def __init__(self, almacenamiento):
        self.almacenamiento = almacenamiento
        self.tareas = self.almacenamiento.cargar()

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        self.almacenamiento.guardar(self.tareas)

    def eliminar_tarea(self, id_tarea):
        self.tareas = [t for t in self.tareas if t.id != id_tarea]
        self.almacenamiento.guardar(self.tareas)

    def buscar_tarea(self, texto):
        resultados = []
        texto_min = texto.lower()
        for t in self.tareas:
            if texto_min in t.titulo.lower() or texto_min in t.descripcion.lower():
                resultados.append(t)
        return resultados
