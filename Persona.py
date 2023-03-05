class Persona:
    def __init__(self, nombre = "", apellido = "", edad = 0, dni = 0):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni

    def mostrar(this):
        print("Persona: {} {} \nDNI: {} \nEdad: {}".format(this.nombre, this.apellido, this.dni, this.edad))

    def esMayor(this):
        return (this.edad >= 18)
    
