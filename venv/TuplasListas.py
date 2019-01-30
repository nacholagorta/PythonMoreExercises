#3. Politiqueo.
#- Escribir una función que reciba una tupla con nombres, y para cada
#nombre imprima el mensaje Estimado <nombre>, vote por mí.
#- Escribir una función que reciba una tupla con nombres, una posición de
#origen p y una cantidad n, e imprima el mensaje anterior para los n
#nombres que se encuentran a partir de la posición p.
#- Modificar las funciones anteriores para que tengan en cuenta el género
#del destinatario, para ello, deberán recibir una tupla de tuplas,
#conteniendo el nombre y el género.

def ejUno():
    tuplaVotantes = ('Andrés', 'Pablo', 'Nacho', 'Alvaro', 'Keloke')
    cont = 0
    for x in tuplaVotantes:
        print("Estimado ", tuplaVotantes[cont]," vote por mí")
        cont = cont + 1

def ejDos() :
        tuplaVotantes = ('Andrés', 'Pablo', 'Nacho', 'Alvaro', 'Keloke')
        pos = input("A partir de que posición quieres mandar el mensaje? : ")
        cant = input("Cuantas veces quieres repetirlo? : ")
        cont = 0
    
        while(cont < int(cant)):

            for x in tuplaVotantes:

                 print("Estimado ", tuplaVotantes[int(pos)], " vote por mí")
                 pos = int(pos) +  1
                 if(pos >=4):
                    SystemExit(0)
        cont = cont +1

def ejTres(personas, origin, cant):
    i = origin -1
    while i < len(personas) and i < cant:
        x = personas[i]
        if x[1] == "Male":
            print("Estimado", x[0], "vote por mi")
        elif x[1] == "Female":
            print("Estimada", x[0], "vote por mi")
        elif x[1] == "Other":
            print("Estimade", x[0], "vote por mi")
        i+=1
personas = (("Juan", "Male"), ("Maria", "Female"), ("Pepe", "Other"))


#ejUno()
#ejDos()
#ejTres(personas, 1, 3)