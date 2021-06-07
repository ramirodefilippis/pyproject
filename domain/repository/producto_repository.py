class productorepository:
    def __init__(self):
        self.__productos=[]
    def ingresar(self, nuevoproducto):
        self.__productos.append(nuevoproducto)
    def consultar(self):
        return self.__productos
    def buscar(self, id):
        return self.__productos[id]
    def eliminar(self, id):
        self.__productos.pop(id)
    def eliminarobjeto(self, producto):
        self.__productos.remove(producto)