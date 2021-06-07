from domain.entity.vendedor import vendedor
from main1 import *

@app.route("/vendedor", methods=["POST", "GET", "DELETE"])
def vendedorapi():
    if request.method=="POST":
        nombre=request.form["nombre"]
        apellido=request.form["apellido"]
        sucursal=request.form["sucursal"]
        turno=request.form["turno"]
        nuevovendedor=vendedor()
        nuevovendedor.ingresardatos(nombre,apellido,sucursal,turno)
        repovendedor.ingresar(nuevovendedor)
        return {"message": "Funciona", "code": 200}
    if request.method=="GET":
        id = int(request.args.get("id"))
        vendedorencontrado = repovendedor.buscar(id)
        return vendedorencontrado.getinfojson()
    if request.method=="DELETE":
        id = int(request.args.get("id"))
        repovendedor.eliminar(id)
        return {"message": "Funciona", "code": 200}