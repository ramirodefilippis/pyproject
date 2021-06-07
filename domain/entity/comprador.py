class comprador:
    def __init__(self,nombre,apellido,dni,telefono):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni
        self.__telefono=telefono

    def getnombre(self):
        return self.__nombre
    def setnombre(self,nuevonombre):
        self.__nombre=nuevonombre

    def getapellido(self):
        return self.__apellido
    def setapellido(self, nuevoapellido):
        self.__apellido=nuevoapellido

    def getdni(self):
        return self.__dni
    def setdni(self,nuevodni):
        self.__dni=nuevodni

    def gettelefono(self):
        return self.__telefono
    def settelefono(self,nuevotelefono):
        self.__telefono=nuevotelefono