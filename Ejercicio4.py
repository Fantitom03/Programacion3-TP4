"""
Se necesita solicitar al usuario el ingreso de datos como nombre, edad, dirección y teléfono. Estos
datos deben ser almacenados en un diccionario llamado usuario_info. Además, se debe permitir el
ingreso de información para varios usuarios. Finalmente, se requiere mostrar la información
ingresada por cada usuario en formato clave-valor.

"""



lista_usuario = []

i = 1
while i != 0:
    usuario_info = {
        "nombre": input("Ingrese Nombre: "),
        "edad": input("Ingrese Edad: "),
        "direccion": input("Ingrese direccion: "),
        "telefono": input("Ingrese telefono: ")

    }
    lista_usuario.append(usuario_info)

    x = int(input("¿QUERES SEGUIR AÑADIENDO USUARIOS?: 1-SI /0-NO \n"))
    i = x


j = 0
for x in lista_usuario:
    j = j+1
    print("\nUSUARIO ", j)
    for clave, valor in x.items():
        print(clave, valor)

