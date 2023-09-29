"""
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa
se bloquee y además explica en un mensaje al usuario la causa y/o solución:
resultado = 15 + "20"
"""

try:
  resultado = 15 + "20"
except:
  print("A ocurrido una excepción. Compruebe si los valores ingresados son números enteros")
