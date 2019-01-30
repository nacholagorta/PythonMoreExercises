
def ej1(dicc = {}):
    diccionario = {}
    if (len(dicc)):
        diccionario = dicc
    nombre = input("Ingresa un nombre: ")
    if nombre in diccionario:
            print("Teléfono actual: ", diccionario[nombre])
            opcion = input("Desea modificar el teléfono?: (1: SI), (2: NO): ")
            if opcion == "1":
                numero = input( "Inserte nuevo teléfono: ")
                diccionario[nombre] = numero
                print("Numero actualizado.")
                return ej1(diccionario)
            if opcion == "2":
                return ej1(diccionario)
    elif nombre == "*":
        sys.exit()

    else:
            numero = input("Inserte teléfono: ")
            diccionario.update({nombre : numero})
            print("Añadido con éxito.")
            return ej1(diccionario)

ej1()