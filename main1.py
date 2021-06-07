# This is a sample Python script.

import requests
from flask import *

from domain.entity.comprador import comprador
from domain.entity.producto import producto
from domain.entity.vendedor import vendedor

app=Flask(__name__,static_url_path="")

productos=[]

vendedores=[]

compradores=[]

@app.route("/")
def ramapadre():
    return {"message":"Funciona","code":200}

from domain.controllers.comprador_controller import *
from domain.controllers.producto_controller import *
from domain.controllers.vendedor_controller import *


if __name__ == '__main__':
    app.run(debug=False, port=5000)

