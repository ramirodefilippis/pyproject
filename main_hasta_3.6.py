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

vendedores=[]

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

@app.route("/producto", methods=["POST", "GET", "DELETE"])
def crearproductopost():
    if request.method=="POST":
        nombre=request.form["nombre"]
        categoria=request.form["categoria"]
        precio=request.form["precio"]
        codigo=request.form["codigo"]
        nuevoproducto=producto()
        nuevoproducto.ingresardatos(nombre,categoria,precio,codigo)
        productos.append(nuevoproducto)
        return {"message": "Funciona", "code": 200}
    if request.method=="GET":
        id = int(request.args.get("id"))
        productoencontrado = productos[id]
        return productoencontrado.getinfojson()
    if request.method=="DELETE":
        id = int(request.args.get("id"))
        productos.pop(id)
        return {"message": "Funciona", "code": 200}

@app.route("/consultarproducto")
def consultarproducto():
    id=int(request.args.get("id"))
    productoencontrado=productos[id]
    return productoencontrado.getinfojson()

@app.route("/crearvendedor")
def crearvendedor():
    nombre=request.args.get("nombre")
    apellido=request.args.get("apellido")
    sucursal=request.args.get("sucursal")
    turno=request.args.get("turno")
    nuevovendedor=vendedor()
    nuevovendedor.ingresardatos(nombre, apellido, sucursal, turno)
    vendedores.append(nuevovendedor)
    return {"message": "Funciona", "code": 200}

@app.route("/consultarvendedor")
def consultarvendedor():
    id=int(request.args.get("id"))
    vendedorencontrado=vendedores[id]
    return vendedorencontrado.getinfojson()

if __name__ == '__main__':
    app.run(debug=False, port=5000)

