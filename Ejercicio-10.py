
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


def generar_estrucutra_list(notas_1, notas_2,nombres):
    nombres = nombres.split(", ")
    alumnos = list(zip(nombres, notas_1, notas_2)) #Genero una lista con tublas la cual va a estar 
    return alumnos                              #conformada por el nombre y sus dos notas correspondientes
  

def generar_estrucutra_dict(notas_1, notas_2,nombres):
    nombres = nombres.split(", ")
    alumnos = {}
    for nombre, nota_1, nota_2 in zip(nombres, notas_1, notas_2): #Con zip genero una tupla con el nombre y sus dos notas
        alumnos[nombre] = (nota_1, nota_2)#Y luego en nombre , nota_1 y nota_2 toman sus valores correspondientes para trabajar el diccionario
    return(alumnos)


def obtener_promedios(estructura):
    return list(map(lambda x: (x[0] + x[1])/2, estructura.values()))
    """Uso map para generar una lista nueva con los resultados de la funcion lambda que 
    lo que hace es tomar de los iterables dos notas y sumarlas para despues dividirla y quedarme con el promedio"""


def promedio_general(promedios):
    return sum(promedios)/len(promedios)


def promedio_mas_alto(promedios,nombres):
    index_max = promedios.index(max(promedios)) #Obtengo el index donde esta el promedio mas alto 
    return nombres.split(", ")[index_max], promedios[index_max] #retorno el nombre


def nota_mas_baja(diccionario):
    notas_sumadas = {nombre: sum(notas) for nombre, notas in diccionario.items()}
    nombre_minimo = min(notas_sumadas, key=notas_sumadas.get)
    return nombre_minimo,min(diccionario[nombre_minimo])




if __name__ == "__main__":
    print("-"*100)

    nueva_estrucutra = generar_estrucutra_dict(notas_1,notas_2,nombres)

    # Imprimir promedios de todos los alumnos
    promedios = obtener_promedios(nueva_estrucutra)
    print("Promedios de todos los alumnos:")
    print(promedios)

    # Imprimir promedio general
    promedio_general = promedio_general(promedios)
    print(f"\nPromedio general: {promedio_general:.2f}")

    # Imprimir alumno con el promedio más alto
    nombre_promedio_max = promedio_mas_alto(promedios, nombres)
    print(f"\nAlumno con el promedio más alto: {nombre_promedio_max[0]}")
    print(f"Promedio: {nombre_promedio_max[1]:.2f}")

    # Imprimir alumno con la nota más baja
    nombre_nota_minima = nota_mas_baja(nueva_estrucutra)
    print(f"\nAlumno con la nota más baja: {nombre_nota_minima[0]}")
    print(f"Nota: {nombre_nota_minima[1]}")

    print("-" * 100)