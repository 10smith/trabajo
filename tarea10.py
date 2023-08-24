#Palíndromos: Un palíndromo es una palabra, frase, número u otro tipo de unidad que se puede leer igual 
#hacia adelante que hacia atrás (ignorando espacios, acentos y signos de puntuación), como "anilina" o 
#"reconocer". Escribe un programa en Python que detecte si una frase dada es un palíndromo. (3pto)

frase = input("ingrese frase: ")
if str(frase) == str(frase) [::-1]:
    print("es palindromo")
else:
    print("no es palindromo")