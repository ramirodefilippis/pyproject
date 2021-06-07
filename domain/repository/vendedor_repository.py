class vendedorrepository:
    def __init__(self):
        self.__vendedores=[]
    def ingresar(self, nuevovendedor):
        self.__vendedores.append(nuevovendedor)
    def consultar(self):
        return self.__vendedores
    def buscar(self, id):
        return self.__vendedores[id]
    def eliminar(self, id):
        self.__vendedores.pop(id)
    def eliminarobjeto(self, vendedor):
        self.__vendedores.remove(vendedor)