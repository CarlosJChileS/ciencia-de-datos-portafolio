def gestion_cursos():
    cursos = {}
    
    while True:
        menu = "Sistema de gestión de curso \n1. Agregar curso \n2. Modificar curso \n3. Mostrar curso \n4. Salir"
        print(menu)
        op = int(input("Escoja una opción: "))

        if op == 1:
            agregar_curso(cursos)

        elif op == 2:
            modificar_curso(cursos)

        elif op == 3:
            mostrar_curso(cursos)

        elif op == 4:
            print("Salió del sistema")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

def agregar_curso(cursos):
    nombre_curso = input("Ingrese el nombre del curso: ")
    estudiantes = input("Ingrese los estudiantes (separados por comas): ").split(',')

    cursos[nombre_curso] = estudiantes

    print("Curso agregado con éxito")

def modificar_curso(cursos):
    nombre_curso = input("Ingrese el nombre del curso que desea modificar: ")

    if nombre_curso in cursos:
        print(f"Estudiantes actuales en {nombre_curso}: {', '.join(cursos[nombre_curso])}")
        accion = input("¿Desea agregar (A) o quitar (Q) estudiantes? ").upper()

        if accion == 'A':
            nuevos_estudiantes = input("Ingrese los nuevos estudiantes (separados por comas): ").split(',')
            cursos[nombre_curso].extend(nuevos_estudiantes)
            print("Estudiantes agregados con éxito")
        elif accion == 'Q':
            estudiantes_a_quitar = input("Ingrese los estudiantes a quitar (separados por comas): ").split(',')
            cursos[nombre_curso] = [estudiante for estudiante in cursos[nombre_curso] if estudiante not in estudiantes_a_quitar]
            print("Estudiantes eliminados con éxito")
        else:
            print("Acción no válida.")
    else:
        print(f"El curso {nombre_curso} no existe.")

def mostrar_curso(cursos):
    for curso, estudiantes in cursos.items():
        print(f"{curso}: {', '.join(estudiantes)}")

gestion_cursos()
