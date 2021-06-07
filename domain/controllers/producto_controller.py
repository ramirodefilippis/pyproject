from domain.entity.producto import producto

@app.route("/producto", methods=["POST", "GET", "DELETE"])
def producto():
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