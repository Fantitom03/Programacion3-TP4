"""
Crear una clase Producto con atributos y métodos relacionados con los productos, una clase
Inventario, la clase Inventario debe tener un atributo de lista para almacenar instancias de la clase
Producto.
Implementar métodos para agregar un producto al inventario, eliminar un producto del inventario
y mostrar el inventario actual.
Pruebe la clase Inventario agregando y eliminando productos del inventario y mostrando el
inventario actualizado.
"""

class Producto:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

class Inventario:
    def __init__(self):

        self.lista_productos = []

    def agregarProducto(self, producto):
        self.lista_productos.append(producto)

    def eliminarProducto(self, id):
        for producto in self.lista_productos:
            if producto.id == id:
                self.lista_productos.remove(producto)
                print(f"Producto con ID {id} eliminado del inventario.")
                return
        print(f"No se encontró un producto con ID {id} en el inventario.")

    def mostrarInventario(self):
        print("\n\nInventario de Productos")
        print("ID\t Nombre\t\t\t Descripcion")
        for producto in self.lista_productos:
            print(producto.id,"\t", producto.nombre,"\t", producto.descripcion)


inventario = Inventario()
producto1 = Producto(1, "Producto_1", "Descripción_del_Producto 1")
producto2 = Producto(2, "Producto_2", "Descripción_del_Producto 2")
producto3 = Producto(3, "Producto_3", "Descripción_del_Producto 3")

inventario.agregarProducto(producto1)
inventario.agregarProducto(producto2)
inventario.agregarProducto(producto3)

inventario.mostrarInventario()

inventario.eliminarProducto(3)
inventario.mostrarInventario()
