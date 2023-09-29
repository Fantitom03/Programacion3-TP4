"""
Ejercicio 1

Realizar un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no
sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de
números y notificarlo:

Concepto útil
La sintaxis [valor] in [lista] permite comprobar si un valor se encuentra en una lista (devuelve True
o False).
"""

lista = [1,2,3,4,5,6,7,8,9]

i = 0
while i != 1:
    x = int(input("Ingrese numero del 0 al 9 \n"))
    if x in lista:
        print("El valor ingresado está en la lista de números")
        i = 1
    else:
        print("El valor ingresado no está en el rango de valores")
        i = 0

