class vendedor:
    def __init__(self):
        self.__nombre=""
        self.__apellido=""
        self.__sucursal=""
        self.__turno=""

    def ingresardatos(self, nombre, apellido, sucursal, turno):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sucursal = sucursal
        self.__turno = turno

    def getnombre(self):
        return self.__nombre
    def setnombre(self,nuevonombre):
        self.__nombre=nuevonombre

    def getapellido(self):
        return self.__apellido
    def setapellido(self, nuevoapellido):
        self.__apellido=nuevoapellido

    def getsucursal(self):
        return self.__sucursal
    def setsucursal(self,nuevasucursal):
        self.__sucursal=nuevasucursal

    def getturno(self):
        return self.__turno
    def setturno(self,nuevoturno):
        self.__turno=nuevoturno

    def getinfojson(self):
        infojson={
            "nombre":self.__nombre,
            "apellido":self.__apellido,
            "sucursal":self.__sucursal,
            "turno":self.__turno
        }
        return infojson