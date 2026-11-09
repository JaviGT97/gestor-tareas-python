# 📝 Gestor de Tareas por Consola

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green.svg)
![Estado](https://img.shields.io/badge/Estado-Estable-brightgreen)

Aplicación de consola en Python para la gestión de tareas personales, desarrollada con una arquitectura sencilla y didáctica que separa la **lógica de negocio**, la **interfaz de usuario** y la **persistencia de datos**.

Ideal como proyecto educativo para aprender estructuración de proyectos Python, manejo de clases, enumeraciones y serialización JSON.

---

## ✨ Características

- ✅ Crear, listar, editar y eliminar tareas
- 🔍 Búsqueda de tareas por título o descripción
- 🏷️ Etiquetas personalizadas separadas por comas
- 🔺 Prioridades: `baja`, `media` y `alta`
- 📅 Fecha límite opcional para cada tarea (formato `YYYY-MM-DD`)
- ✔️ Marcado de tareas como completadas
- 💾 Persistencia automática en formato JSON
- 🛡️ Recuperación robusta ante archivos JSON corruptos

---

## 🏗️ Estructura del proyecto

```
gestor-tareas-python/
├── run_console.py        # Punto de entrada de la aplicación
├── todo/                 # Paquete principal
│   ├── __init__.py
│   ├── consola.py        # Interfaz de usuario por consola
│   ├── modelo.py         # Modelo de datos (Tarea, Prioridad, GestorTareas)
│   └── storage.py        # Capa de persistencia (SerializadorJSON)
├── data/
│   └── tareas.json       # Almacenamiento de datos (se genera automáticamente)
└── README.md
```

### Separación de responsabilidades

| Módulo | Responsabilidad |
|---|---|
| `consola.py` | Menú interactivo y entrada/salida con el usuario |
| `modelo.py` | Clases `Tarea`, `Prioridad` y `GestorTareas` (lógica de negocio) |
| `storage.py` | Lectura y escritura del archivo JSON |

---

## 🚀 Instalación

Requiere **Python 3.8 o superior**. No necesita dependencias externas (solo la biblioteca estándar).

```bash
# 1. Clona el repositorio
git clone https://github.com/JaviGT97/gestor-tareas-python.git

# 2. Entra al directorio
cd gestor-tareas-python

# 3. Ejecuta la aplicación
python run_console.py
```

---

## 🖥️ Uso

Al ejecutar la aplicación se muestra un menú interactivo:

```
==== GESTOR DE TAREAS CONSOLA ====
1. Listar tareas
2. Añadir tarea
3. Editar tarea
4. Eliminar tarea
5. Marcar tarea como completada
6. Buscar tarea
7. Guardar y salir
Seleccione una opción:
```

### Ejemplo de listado

```
--- LISTADO DE TAREAS ---
[X] Comprar leche | ID: a1b2c3d4 | Prioridad: alta | Límite: 2026-11-15
[ ] Estudiar Python | ID: e5f6a7b8 | Prioridad: media | Límite: Sin límite
```

> 💡 Para editar, eliminar o completar una tarea solo necesitas escribir los **primeros caracteres de su ID**.

---

## 📦 Formato de datos

Las tareas se guardan en `data/tareas.json`:

```json
[
    {
        "id": "a1b2c3d4-e5f6-...",
        "titulo": "Estudiar Python",
        "descripcion": "Repasar clases y enums",
        "fecha_creacion": "2026-11-09T10:30:00",
        "fecha_limite": "2026-11-20",
        "prioridad": "media",
        "etiquetas": ["estudio", "python"],
        "completada": false
    }
]
```

---

## 🎓 Conceptos aplicados

Este proyecto es útil para aprender o repasar:

- **Programación orientada a objetos**: clases, métodos y encapsulación
- **Enumeraciones** (`enum.Enum`) para valores acotados como la prioridad
- **Serialización JSON** con `json` y codificación UTF-8
- **Generación de identificadores únicos** con `uuid.uuid4()`
- **Manejo de excepciones** ante archivos corruptos (`JSONDecodeError`)
- **Arquitectura en capas**: separación entre UI, lógica y persistencia

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Algunas ideas de mejora:

- [ ] Añadir tests unitarios con `pytest`
- [ ] Validar el formato de la fecha límite
- [ ] Exportar tareas a CSV o Markdown
- [ ] Interfaz web con Flask o interfaz gráfica con Tkinter

## 📄 Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).
