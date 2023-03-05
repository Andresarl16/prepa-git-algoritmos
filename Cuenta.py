class Cuenta:
    def __init__(self, titular = None, bono = 0, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad
        self.bono = bono

    def getTitular(this):
        return this.titular

    def setTitular(this, nuevoTitular):
        this.titular = nuevoTitular

    def getBono(this):
        return this.bono

    def setBono(this, nuevoBono):
        this.bono = nuevoBono

    def getMonto(this):
        return this.monto

    def setMonto(this, nuevoMonto):
        this.monto = nuevoMonto

    def mostrar(this):
        this.titular.mostrar()
        print("Cantidad: ", this.cantidad, this.bono)

    def ingresar(self, cantidad):
        if(cantidad > 0):
            self.cantidad += cantidad
        else:
            print("Ingreso un monto invalido.")

    def retirar(self, cantidad):
        self.cantidad -= cantidad
        