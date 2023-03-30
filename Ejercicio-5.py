import string

frase = input("Ingrese una frase: ")
string = input("Ingrese una palabra: ").lower()

frase2 = frase.lower().split()



print(frase2)

resultado = 0
for palabra in frase.lower().split():
    if(string == palabra.strip(",")):
        resultado+=1

print("-"*30)
print("Frase: {}".format(frase))
print("Palabra: {}".format(string))
print("Restulado: {}".format(resultado))
print("-"*30)