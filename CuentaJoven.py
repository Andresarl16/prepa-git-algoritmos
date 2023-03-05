from Cuenta import *

class CuentaJoven(Cuenta):
    def __init__(self, titular = None, cantidad = 0, bonificacion = 0):
        Cuenta.__init__(self, titular, cantidad)
        self.bonificacion = bonificacion

    def getBonificacion(this):
        return this.bonificacion

    def setBonificacion(this, nuevaBonificacion):
        this.bonificacion = nuevaBonificacion
    
    def mostrar(this):
        Cuenta.mostrar(this)
        print("Bonificacion: ", this.bonificacion, "%")

    def esTitularValido(self):
        if(self.titular.edad >= 18 and self.titular.edad < 25):
            return True
        else:
            return False

    def retirar(self, cantidad):
        if(self.esTitularValido()):
            self.cantidad -= cantidad
        else:
            print("El titular no es valido")   