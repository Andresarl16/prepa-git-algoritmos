class Cuenta:
    def __init__(self, titular=None, cantidad=0, numeroDeCuenta=0):
        self.titular = titular
        self.cantidad = cantidad
        self.numeroDeCuenta = numeroDeCuenta

    def getTitular(this):
        return this.titular

    def setTitular(this, nuevoTitular):
        this.titular = nuevoTitular

    def getMonto(this):
        return this.monto

    def setMonto(this, nuevoMonto):
        this.monto = nuevoMonto

    def getNumeroDeCuenta(this):
        return this.numeroDeCuenta

    def setNumeroDeCuenta(this, numeroDeCuenta):
        this.numeroDeCuenta = numeroDeCuenta

    def mostrar(this):
        this.titular.mostrar()

        if (this.numeroDeCuenta % 2 == 0):
            this.cantidad *= 2
        else:
            this.cantidad += 200

        print("Cantidad: ", this.cantidad, this.numeroDeCuenta)

    def ingresar(self, cantidad):
        if (cantidad > 0):
            self.cantidad += cantidad
        else:
            print("Ingreso un monto invalido.")

    def retirar(self, cantidad):
        self.cantidad -= cantidad
