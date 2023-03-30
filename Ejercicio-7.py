texto = """
 El salario promedio de un hombre en Argentina es de $60.000, mientras que 
el de una mujer es de $45.000. Además, las mujeres tienen menos 
posibilidades de acceder a puestos de liderazgo en las empresas.
"""

mayusculas = 0
minusculas = 0
no_letras = 0
palabras = len(texto.split())


for palabra in texto:
    if(palabra.isupper()):
        mayusculas+=1
    if(palabra.islower()):
        minusculas+=1
    if(not palabra.isalpha() and (not palabra.isspace())):
        no_letras+=1

# Imprimir resultados
print("Mayúsculas: {}".format(mayusculas))
print("Minúsculas: {}".format(minusculas))
print("No letras: {}".format(no_letras))
print("Palabras: {}".format(palabras))