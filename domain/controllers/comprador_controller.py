from domain.entity.comprador import comprador

@app.route("/comprador", methods=["POST", "GET", "DELETE"])
def comprador():
    if request.method=="POST":
        nombre=request.form["nombre"]
        apellido=request.form["apellido"]
        dni=request.form["dni"]
        telefono=request.form["telefono"]
        nuevocomprador=compradores()
        nuevocomprador.ingresardatos(nombre,apellido,dni,telefono)
        compradores.append(nuevocomprador)
        return {"message": "Funciona", "code": 200}
    if request.method=="GET":
        id = int(request.args.get("id"))
        compradorencontrado = compradores[id]
        return compradorencontrado.getinfojson()
    if request.method=="DELETE":
        id = int(request.args.get("id"))
        compradores.pop(id)
        return {"message": "Funciona", "code": 200}