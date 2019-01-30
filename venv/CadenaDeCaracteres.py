
#Inserte el carácter entre cada letra de la cadena. Ej: ’separar’ y ’,’debería devolver : ’s,e,p,a,r,a,r’
def ejUno():
    cad = input("Frase: ")
    caracter = input("Caracter: ")
    print (caracter.join(cad))

#Reemplace todos los espacios por el carácter. Ej: ’mi archivo de texto.txt’ y ’_’ debería devolver ’mi_archivo_de_texto.txt’
def ejDos():
    cad = input("Frase: ")
    caracter = input("Caracter: ")
    print(cad.replace(" ", caracter))

#Reemplace todos los dígitos en la cadena por el carácter. Ej: ’su clave es: 1540’ y ’X’ debería devolver ’su clave es: XXXX’
def ejTres():
    cad = input("Frase:")
    caracter = input("Caracter:")
    for i in range(0, 9):
        cad = cad.replace(str(i), caracter)
    print(cad)

#Inserte el caracter cada 3 dígitos en la cadena. Ej. ’2552552550’ y ’.’ debería devolver ’255.255.255.0’
def ejCuatro():
    cad = input("Número:")
    car = input("Caracter:")
    cont = 0
    cad2 = ""
    for x in cad:
        if cont != 0 and cont % 3 == 0:
            cad2 += car
        cad2 += x
        cont = cont + 1
    print(cad2)

#Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, ’cadena’ es una subcadena de ’subcadena’.
def ejCinco():
    cad1 = input("Frase uno:")
    cad2 = input("Frase dos:")

    if cad1.find(cad2) > -1:
        print("La segunda frase es subcadena de la primera")
    else:
        print("La segunda frase no es subcadena de la primera")

#Devuelva la que sea anterior en orden alfabético. Por ejemplo, si recibe ’kde’ y ’gnome’ debe devolver ’gnome’.
def ejSeis():
    cad1 = input("Frase uno:")
    cad2 = input("Frase dos:")

    if cad1 < cad2:
        print(cad1)
    else:
        print(cad2)

        #Llamadas de prueba comentadas con '#', para probar la app descomentar

#ejUno()
#ejDos()
#ejTres()
#ejCuatro()
#ejCinco()
#ejSeis()