from domain.entity.producto import producto
from main1 import *


@app.route("/producto", methods=["POST", "GET", "DELETE"])
def productoapi():
    if request.method=="POST":
        nombre=request.form["nombre"]
        categoria=request.form["categoria"]
        precio=request.form["precio"]
        codigo=request.form["codigo"]
        nuevoproducto=producto()
        nuevoproducto.ingresardatos(nombre,categoria,precio,codigo)
        repoproducto.ingresar(nuevoproducto)
        return {"message": "Funciona", "code": 200}
    if request.method=="GET":
        id = int(request.args.get("id"))
        productoencontrado=repoproducto.buscar(id)
        return productoencontrado.getinfojson()
    if request.method=="DELETE":
        id = int(request.args.get("id"))
        repoproducto.eliminar(id)
        return {"message": "Funciona", "code": 200}