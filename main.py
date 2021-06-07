# This is a sample Python script.

import requests
from flask import *
app=Flask(__name__,static_url_path="")
from domain.entity.comprador import comprador
from domain.entity.producto import producto
from domain.entity.vendedor import vendedor

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

pepe=comprador("carlos","perez",20202020,154123654)

productos=[]

juan=vendedor("juan","lopez","avellaneda","mañana")

def inicio():
    print(pepe.getnombre())
    print(pepe.getapellido())
    pepe.setnombre(nuevonombre="carlos")
    print(pepe.getnombre())

@app.route("/")
def ramapadre():
    return {"message":"Funciona","code":200}

@app.route("/comprador")
def comprador():
    return pepe.getnombre()

@app.route("/mostrarnombre")
def mostrarnombre():
    nombre=request.args.get("nombre")
    apellido=request.args.get("apellido")
    texto="hola " + nombre + " " + apellido
    return texto

@app.route("/crearproducto")
def crearproducto():
    nombre=request.args.get("nombre")
    categoria=request.args.get("categoria")
    precio=int(request.args.get("precio"))
    codigo=int(request.args.get("codigo"))
    nuevoproducto=producto()
    nuevoproducto.ingresardatos(nombre,categoria,precio,codigo)
    productos.append(nuevoproducto)
    return {"message": "Funciona", "code": 200}

@app.route("/consultarproducto")
def consultarproducto():
    id=int(request.args.get("id"))
    productoencontrado=productos[id]
    return productoencontrado.getinfojson()

if __name__ == '__main__':
    app.run(debug=False, port=5000)

