
nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David',
'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 
'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge',
'JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa', 
'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás',  'Nancy', 'Noelia', 'Pablo', 
'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12,
13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18,
74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64,
87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15,
39, 15, 74, 33, 57, 10]


def generar_estrucutra(notas_1, notas_2,nombres):
    nombres = nombres.split(", ")

    alumnos = list(zip(nombres, notas_1, notas_2)) #Genero una lista con tublas la cual va a estar 
                                                    #conformada por el nombre y sus dos notas correspondientes
    
    return alumnos

def generar_estrucutra2(notas_1, notas_2,nombres):
    
    nombres = nombres.split(", ")
    
    alumnos = {}
    
    for nombre, nota_1, nota_2 in zip(nombres, notas_1, notas_2): #Con zip genero una tupla con el nombre y sus dos notas
                    #Y luego en nombre , nota_1 y nota_2 toman sus valores correspondientes para trabajar el diccionario
    
        alumnos[nombre] = (nota_1, nota_2)
    
    return(alumnos)

def obtener_promedios(notas_1, notas_2):
    return list(map(lambda x,y:(x+y)/2,notas_1,notas_2))
"""Uso map para generar una lista nueva con los resultados de la funcion lambda que 
lo que hace es tomar de los iterables dos notas y sumarlas para despues dividirla y quedarme con el promedio"""

def promedio_general(notas_1, notas_2s):
    return sum(obtener_promedios(notas_1,notas_2))/len(notas_1)

def promedio_mas_alto(notas_1, notas_2, nombres):
    promedios = obtener_promedios(notas_1,notas_2)
    index_max = promedios.index(max(promedios)) #Obtengo el index donde esta el promedio mas alto 
    return nombres[index_max] #retorno el nombre


print(generar_estrucutra(notas_1, notas_2, nombres))