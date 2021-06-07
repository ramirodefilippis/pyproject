class producto:
    def __init__(self):
        self.__nombre=""
        self.__categoria=""
        self.__precio=""
        self.__codigo=""

    def ingresardatos(self,nombre,categoria,precio,codigo):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__codigo = codigo

    def getnombre(self):
        return self.__nombre
    def setnombre(self,nuevonombre):
        self.__nombre=nuevonombre

    def getcategoria(self):
        return self.__categoria
    def setcategoria(self, nuevacategoria):
        self.__categoria=nuevacategoria

    def getprecio(self):
        return self.__precio
    def setprecio(self,nuevoprecio):
        self.__precio=nuevoprecio

    def getcodigo(self):
        return self.__codigo
    def setcodigo(self,nuevocodigo):
        self.__codigo=nuevocodigo

    def getinfojson(self):
        infojson={
            "nombre":self.__nombre,
            "categoria":self.__categoria,
            "precio":self.__precio,
            "codigo":self.__codigo
        }
        return infojson