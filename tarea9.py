#Cifrado César: El cifrado César es una técnica de cifrado simple en la que cada letra en el texto original se 
#reemplaza por una letra un cierto número de posiciones más adelante en el alfabeto. Por ejemplo, con un 
#desplazamiento de 1, "A" se reemplazaría por "B", "B" se convertiría en "C", etc. Escribe un programa que 
#implemente el cifrado César para un mensaje y un desplazamiento dados. (5pto)

mesaje = input("ingrese mesaje:").upper()
n_desplazamineto = int (input("ingrese desplazamiento:"))

abc = "ABCDFGHIJKLMNÑOPQRSTUVWXYZ"

cifrado = " "
for k in mesaje:
    if k in abc:
        pos_letra = abc.index(k)
        nueva_pos = (pos_letra+n_desplazamineto)% len(abc)
        cifrado += abc [nueva_pos]
    else:
        cifrado +=k
print("mensaje sifrado cesar:", cifrado)

