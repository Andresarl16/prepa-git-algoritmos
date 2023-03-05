'''

Ejercicio 5.2

Cree una clase llamada Cuenta que tenga los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). 
El titular será obligatorio y la cantidad es opcional. 

Construya los siguientes métodos para la clase:

- Un constructor.
- Los setters y getters para cada uno de los atributos.
- mostrar() que muestra los datos de la cuenta.
- ingresar(cantidad) que ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, se le indica al usuario que ingreso un monto invalido.
- retirar(cantidad) que retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
'''

from Cuenta import *
from Persona import *

persona1 = Persona("Andrea", "Contreras", 27, 1)

cuenta = Cuenta(persona1, 20)

cuenta.mostrar()
cuenta.retirar(10)
cuenta.ingresar(-500)
cuenta.ingresar(500)
cuenta.mostrar()