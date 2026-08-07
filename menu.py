modificar_platillo(menu):
    """U - Update: Modifica los datos de un platillo existente."""

    limpiar_pantalla()
    print("===== MODIFICAR PLATILLO =====")

    codigo = input("Ingrese el código del platillo: ").strip()

    for platillo in menu:

        if platillo["codigo"] == codigo:

            nombre = input(f"Nombre ({platillo['nombre']}): ").strip()
            if nombre:
                platillo["nombre"] = nombre

            print("\nSeleccione la nueva categoría")
            print("1. Desayuno")
            print("2. Almuerzo")
            print("3. Cena")
            print("ENTER para dejar la misma")
            opcion = input("Opción: ").strip()

            if opcion == "1":
                platillo["categoria"] = "Desayuno"
            elif opcion == "2":
                platillo["categoria"] = "Almuerzo"
            elif opcion == "3":
                platillo["categoria"] = "Cena"
            elif opcion == "4":

            precio = input(f"Precio ({platillo['precio']}): ").strip()
            if precio:
                try:
                    platillo["precio"] = float(precio)
                except ValueError:
                    print("Precio inválido.")

            disponible = input("Disponible (S/N): ").strip().upper()
            if disponible == "S":
                platillo["disponible"] = True
            elif disponible == "N":
                platillo["disponible"] = False

            guardar_menu(menu)

            print("\nPlatillo actualizado correctamente.")
            input("Presione ENTER para continuar...")
            return

    print("Platillo no encontrado.")
    input("Presione ENTER para continuar...")
