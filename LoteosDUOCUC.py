import numpy as np
import random  

#Variables glabales
tabla = np.array([[' ', ' ', ' ',' ',' '], [' ', ' ', ' ',' ',' '], [' ', ' ', ' ',' ',' '],[' ', ' ', ' ',' ',' ']])
lotes_seleccionados = []
clientes = []

#definicion para mostrar los lotes
def mostrar_lotes():  
    print("   1.   2.   3.   4.   5.    ")
    print("1. {}  | {}  | {}  | {}  | {} ".format(tabla[0][0], tabla[0][1], tabla[0][2], tabla[0][3], tabla[0][4]))
    print("  -------------------------")
    print("2. {}  | {}  | {}  | {}  | {} ".format(tabla[1][0], tabla[1][1], tabla[1][2], tabla[1][3], tabla[1][4]))
    print("  -------------------------")
    print("3. {}  | {}  | {}  | {}  | {} ".format(tabla[2][0], tabla[2][1], tabla[2][2], tabla[2][3], tabla[2][4]))
    print("  --------------------------")
    print("4. {}  | {}  | {}  | {}  | {} ".format(tabla[3][0], tabla[3][1], tabla[3][2], tabla[3][3], tabla[3][4]))
    print("  -------------------------")


#definicion para mostrar los lotes dispobiles
def mostrar_lotes_disponibles():
    print("Lotes Disponibles: ")
    mostrar_lotes()

#definicion para seleccionar lote/confirmacion o no
def seleccion_lote():
    mostrar_lotes_disponibles()
    fila = int(input("Ingrese el número de fila del lote (1-4):  "))
    columna = int(input("Ingrese el número de columna del lote (1-5): "))
    
    if fila < 1 or fila > len(tabla) or columna < 1 or columna > len(tabla[0]):
        print("Coordenadas inválidas. Inténtelo de nuevo.")
        return
    
    if tabla[fila-1][columna-1] == ' ':
        confirmacion = int(input("Desea confirmar la selección y compra del lote? 1. SI - 2. NO: "))
        if confirmacion == 1:
                lote = {
                'fila': fila,
                'columna': columna,
                }
        
                lotes_seleccionados.append(lote)
                tabla[fila-1][columna-1] = 'X'
                    
                ver_detalle = int(input("Desea ver los detalles del lote seleccionado? 1. SI - 2. NO: "))
                if ver_detalle == 1:
                        mostrar_detalles_lote()
                else: 
                    ("")
                print("Por favor ingrese sus datos")
                rut = input("Ingrese su RUT: ")
                nombre = input("Ingrese su nombre completo: ")
                telefono = input("Ingrese su teléfono: ")
                email = input("Ingrese su correo electrónico: ")

                cliente = {
                'rut': rut,
                'nombre': nombre,
                'telefono': telefono,
                'email': email
                }

                clientes.append(cliente)
        
                print("Lote seleccionado exitosamente.")
        else:
            print("Selección de lote cancelada.")
    else:
        print("El lote seleccionado no está disponible.")

#definicion para mostrar los detalles del lote comprado
def mostrar_detalles_lote():
    if lotes_seleccionados:
        for lote in lotes_seleccionados:
            print("Lote seleccionado: Fila {}, Columna {}".format(lote['fila'], lote['columna']))
            print("Detalles del lote:")
            print("Medidas: {} Metros Cuadrados".format(random.randint(1500, 2500)))
            print("Características: {}".format(obtener_caracteristicas_aleatorias()))
            print("Precio: {} CLP".format(obtener_precio_lote()))
            print()
    else:
        print("No se han seleccionado lotes.")

#definicion para generar caracteristicas del lote
def obtener_caracteristicas_aleatorias():
    caracteristicas = ["Salida a entrada Princpal", "Desnivel Leve", "Desnivel en pendiente", "Acceso a Rio Blanco", "Lote con Conexion a Luz y Agua"]
    num_caracteristicas = random.randint(1, 3)
    return random.sample(caracteristicas, num_caracteristicas)

def obtener_precio_lote():
    precios_lote = ["35.000.000", "45.000.000", "50.000.000", "55.000.000", "60.000.000", "65.000.000", "70.000.000"]
    return random.sample(precios_lote,1)

#definicion para mostrar los clientes que han comprado lote
def mostrar_clientes():
    if clientes:
        print("Clientes:")
        for cliente in clientes:
            print("RUT: {}".format(cliente['rut']))
            print("Nombre: {}".format(cliente['nombre']))
            print("Teléfono: {}".format(cliente['telefono']))
            print("Correo electrónico: {}".format(cliente['email']))
            print()
    else:
        print("No hay clientes registrados.")

#definicion de menu principal de compra
def Menu_loteDuoc():
    while True:
        print("=== MENÚ ===")
        print("1. Ver disponibilidad de lotes")
        print("2. Seleccionar un lote")
        print("3. Ver detalles del lote seleccionado")
        print("4. Ver clientes")
        print("5. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            mostrar_lotes_disponibles()
        elif opcion == 2:
            seleccion_lote()
        elif opcion == 3:
            mostrar_detalles_lote()
        elif opcion == 4:
            mostrar_clientes()
        elif opcion == 5:
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")
Menu_loteDuoc()
