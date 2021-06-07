from domain.entity.vendedor import vendedor
from main1 import *

@app.route("/vendedor", methods=["POST", "GET", "DELETE"])
def vendedor():
    if request.method=="POST":
        nombre=request.form["nombre"]
        apellido=request.form["apellido"]
        sucursal=request.form["sucursal"]
        turno=request.form["turno"]
        nuevovendedor=vendedor()
        nuevovendedor.ingresardatos(nombre,apellido,sucursal,turno)
        vendedores.append(nuevovendedor)
        return {"message": "Funciona", "code": 200}
    if request.method=="GET":
        id = int(request.args.get("id"))
        vendedorencontrado = vendedores[id]
        return vendedorencontrado.getinfojson()
    if request.method=="DELETE":
        id = int(request.args.get("id"))
        vendedores.pop(id)
        return {"message": "Funciona", "code": 200}