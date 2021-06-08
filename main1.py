# This is a sample Python script.

import requests
from flask import *
from flasgger import Swagger
from flasgger import swag_from

from domain.entity.comprador import comprador
from domain.entity.producto import producto
from domain.entity.vendedor import vendedor

from domain.repository.producto_repository import productorepository
from domain.repository.vendedor_repository import vendedorrepository
from domain.repository.comprador_repository import compradorrepository

app=Flask(__name__,static_url_path="")
swagger = Swagger(app)

repoproducto=productorepository()

repovendedor=vendedorrepository()

repocomprador=compradorrepository()

@app.route("/")
@swag_from("info.yml")
def ramapadre():
    return {"message":"Funciona","code":200}


from domain.controllers.comprador_controller import *
from domain.controllers.producto_controller import *
from domain.controllers.vendedor_controller import *


if __name__ == '__main__':
    app.run(debug=False, port=5000)

