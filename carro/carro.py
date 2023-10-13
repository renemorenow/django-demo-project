class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        self.carro = carro


    def agregar(self, producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[str(producto.id)] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": float(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            self.carro[str(producto.id)]["cantidad"] += 1
            self.carro[str(producto.id)]["precio"] += float(producto.precio)
        self.guardar_carro()


    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True


    def eliminar(self, producto):
        if str(producto.id) in self.carro.keys():
            del self.carro[str(producto.id)]
            self.guardar_carro()


    def restar_producto(self, producto):
        if str(producto.id) in self.carro.keys():
            self.carro[str(producto.id)]["cantidad"] -= 1
            self.carro[str(producto.id)]["precio"] -= float(producto.precio)
            if self.carro[str(producto.id)]["cantidad"] < 1:
                self.eliminar(producto)
            self.guardar_carro()


    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True
