import json
import os

ARCHIVO_JSON = 'menu_restaurante.json'

def limpiar_pantalla():
    """Limpia la consola para mantener una interfaz limpia."""
    pass

def cargar_menu():
    """Carga los datos del menú desde el archivo JSON."""
    pass

def guardar_menu(menu):
    """Guarda los datos del menú en el archivo JSON."""
    pass

def registrar_platillo(menu):
    """C - Create: Registra un nuevo platillo."""
    pass

def consultar_platillos(menu):
    """R - Read: Muestra el catálogo de platillos."""
    pass

def modificar_platillo(menu):
    """U - Update: Modifica los datos de un platillo existente."""
    pass

def eliminar_platillo(menu):
    """D - Delete: Elimina un platillo del menú."""
    pass

def mostrar_menu_principal():
    """Muestra la interfaz principal del sistema y controla el flujo."""
    menu = cargar_menu()
    
    while True:
        limpiar_pantalla()
        print("========================================")
        print("      SISTEMA DE GESTIÓN DE MENÚ")
        print("========================================")
        print("1. Registrar nuevo platillo")
        print("2. Consultar menú")
        print("3. Modificar platillo")
        print("4. Eliminar platillo")
        print("5. Salir del sistema")
        print("========================================")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == '1':
            registrar_platillo(menu)
        elif opcion == '2':
            consultar_platillos(menu)
        elif opcion == '3':
            modificar_platillo(menu)
        elif opcion == '4':
            eliminar_platillo(menu)
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione ENTER para continuar...")

if __name__ == "__main__":
    mostrar_menu_principal()