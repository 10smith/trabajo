#Contar caracteres y palabras: Dada la siguiente frase: "Estoy aprendiendo Python y me está 
#gustando mucho. ¡Es genial!". Escribe un programa en Python que cuente el número de palabras y de 
#caracteres (incluyendo espacios y signos de puntuación). (3pto) 

frase = " estoy aorendiendo en python y me esta guatando ""genial"

num_palabra = frase.split()
numero_de_palabras = len(num_palabra)

numero_de_caracteres = len(frase)

print("numero de caracteres :", numero_de_caracteres)
print("numero de palabras:", numero_de_palabras)
