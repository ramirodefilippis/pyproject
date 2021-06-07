class compradorrepository:
    def __init__(self):
        self.__compradores=[]
    def ingresar(self, nuevocomprador):
        self.__compradores.append(nuevocomprador)
    def consultar(self):
        return self.__compradores
    def buscar(self, id):
        return self.__compradores[id]
    def eliminar(self, id):
        self.__compradores.pop(id)
    def eliminarobjeto(self, comprador):
        self.__compradores.remove(comprador)