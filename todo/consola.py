from todo.modelo import GestorTareas, Tarea, Prioridad
from todo.storage import SerializadorJSON


def mostrar_menu():
    print("\n==== GESTOR DE TAREAS CONSOLA ====")
    print("1. Listar tareas")
    print("2. Añadir tarea")
    print("3. Editar tarea")
    print("4. Eliminar tarea")
    print("5. Marcar tarea como completada")
    print("6. Buscar tarea")
    print("7. Guardar y salir")
    return input("Seleccione una opción: ")


def iniciar_consola():
    almacenamiento = SerializadorJSON("data/tareas.json")
    gestor = GestorTareas(almacenamiento)

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            print("\n--- LISTADO DE TAREAS ---")
            for t in gestor.tareas:
                estado = "[X]" if t.completada else "[ ]"
                limite = t.fecha_limite if t.fecha_limite else "Sin límite"
                print(
                    f"{estado} {t.titulo} | ID: {t.id[:8]} | Prioridad: {t.prioridad} | Límite: {limite}")

        elif opcion == "2":
            titulo = input("Título (obligatorio): ").strip()
            while not titulo:
                print("Error: El título no puede estar vacío.")
                titulo = input("Título (obligatorio): ").strip()

            descripcion = input("Descripción: ")
            limite = input("Fecha límite (YYYY-MM-DD): ")
            limite = limite if limite else None
            prioridad = input("Prioridad (baja/media/alta): ").lower()
            if prioridad not in [p.value for p in Prioridad]:
                prioridad = Prioridad.MEDIA.value
            etiquetas_str = input("Etiquetas (separadas por coma): ")
            etiquetas = [e.strip()
                         for e in etiquetas_str.split(",") if e.strip()]

            nueva = Tarea(titulo, descripcion, limite, prioridad, etiquetas)
            gestor.agregar_tarea(nueva)
            print("Tarea guardada correctamente.")

        elif opcion == "3":
            id_tarea = input("Ingrese el inicio del ID de la tarea a editar: ")
            tarea = next(
                (t for t in gestor.tareas if t.id.startswith(id_tarea)), None)
            if tarea:
                nuevo_titulo = input(
                    f"Nuevo título (actual: {tarea.titulo}) [Enter para no cambiar]: ").strip()
                if nuevo_titulo:
                    tarea.editar(titulo=nuevo_titulo)

                nueva_desc = input(
                    f"Nueva descripción (actual: {tarea.descripcion}) [Enter para no cambiar]: ").strip()
                if nueva_desc:
                    tarea.editar(descripcion=nueva_desc)

                gestor.almacenamiento.guardar(gestor.tareas)
                print("Tarea actualizada.")
            else:
                print("No se encontró ninguna tarea con ese ID.")

        elif opcion == "4":
            id_tarea = input(
                "Ingrese el inicio del ID de la tarea a eliminar: ")
            tarea = next(
                (t for t in gestor.tareas if t.id.startswith(id_tarea)), None)
            if tarea:
                confirmacion = input(
                    "¿Confirma que desea eliminar esta tarea? (S/N): ").upper()
                if confirmacion == "S":
                    gestor.eliminar_tarea(tarea.id)
                    print("Tarea eliminada.")
            else:
                print("No se encontró ninguna tarea con ese ID.")

        elif opcion == "5":
            id_tarea = input(
                "Ingrese el inicio del ID de la tarea a completar: ")
            tarea = next(
                (t for t in gestor.tareas if t.id.startswith(id_tarea)), None)
            if tarea:
                tarea.marcar_completada()
                gestor.almacenamiento.guardar(gestor.tareas)
                print("Tarea marcada como completada.")
            else:
                print("No se encontró ninguna tarea con ese ID.")

        elif opcion == "6":
            texto = input("Texto a buscar en título o descripción: ")
            encontradas = gestor.buscar_tarea(texto)
            if encontradas:
                print("\n--- RESULTADOS DE BÚSQUEDA ---")
                for t in encontradas:
                    estado = "[X]" if t.completada else "[ ]"
                    print(f"{estado} {t.titulo} | ID: {t.id[:8]}")
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "7":
            gestor.almacenamiento.guardar(gestor.tareas)
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")
