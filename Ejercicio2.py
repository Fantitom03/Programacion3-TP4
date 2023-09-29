"""
Realiza un programa que siga las siguientes instrucciones:
• Crea un conjunto llamado usuarios con los usuarios Marcela, David, Elvira, Juan y Marcos
• Crea un conjunto llamado administradores con los administradores Juan y Marcela.
• Borra al administrador Juan del conjunto de administradores.
• Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
• Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada
usuario es administrador o no.
Sugerencia
Los conjuntos se pueden recorrer dinámicamente utilizando el bucle for de forma similar a una lista.
También cuentan con un método llamado .discard(elemento) que sirve para borrar o descartar un
elemento.

"""

usuarios = set()
#Lista de usuarios
usuarios.add("Marcela")
usuarios.add("David")
usuarios.add("Elvira")
usuarios.add("Juan")
usuarios.add("Marcos")
#print(usuarios)

administradores = set()

#Lista de administradores inicial
administradores.add("Juan")
administradores.add("Marcela")
#print(administradores)

#Se elimina a Juan de la lista administradores
administradores.discard("Juan")
#print(administradores)

#Se añade a Marcos a la lista administradores
administradores.add("Marcos")
#print(administradores)

for usuario in usuarios:
    if usuario in administradores:
        print(usuario+"     Adminstrador")
    else:
        print(usuario + "      Usuario")





