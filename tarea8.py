#inversion de palabras en una frase : Dada la frase " aprendiento python con Edem". EScribe un 
#programa que inverta el orden de las palabras en la frase, pero mantenga el orden de los caracteres en cada
#palabra. El resultado deveria ser :"Edem con python aprendiendo". (3.pto)

frase = " Aprendiendo python con Edem"
palabras = frase.split()
frase_invertivo = " ".  join(reversed(palabras))
print(frase_invertivo)