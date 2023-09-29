"""
Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas
ordenadas. La primera con los números pares y la segunda con los números impares.
Por ejemplo:
pares, impares = separar([6,5,2,1,7])
print(pares)
print(impares)
[2, 6]
[1, 5, 7]
Sugerencia
Para ordenar una lista automáticamente puedes utilizar el método .sort().
"""


lista_desordenada = [1,8,6,2,7,5,4,9]
def separar(lista):
    lista.sort()

    pares=[]
    impares=[]

    numero =0
    for element in lista:
        if numero % 2 == 0:
            pares.append(element)
        else:
            impares.append(element)
        numero +=1
    print(pares, impares)

separar(lista_desordenada)