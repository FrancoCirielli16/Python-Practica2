
def es_heterograma(palabra_o_frase):
    
    letras_vistas = set()
    for letra in palabra_o_frase:
        if letra.isalpha():
            if letra.lower() in letras_vistas:
                return False
            else:
                letras_vistas.add(letra.lower())
    return True


palabra_o_frase = input("Ingrese una palabra o frase: ")



if es_heterograma(palabra_o_frase):
    print("La palabra/frase es un heterograma.")
else:
    print("La palabra/frase no es un heterograma.")