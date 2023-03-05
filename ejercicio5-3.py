'''

Ejercicio 5.3

Ahora se le pide que cree una “Cuenta Joven”, para ello debe crear una nueva clase CuentaJoven que herede de la clase Cuenta. 
Cuando se crea esta nueva clase, además del titular y la cantidad, se debe guardar una bonificación que estará expresada en tanto por ciento.

Construye los siguientes métodos para la clase:

- Un constructor.
- Los setters y getters para cada uno de los nuevos atributos.
- esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
- retirar(cantidad) que retira una cantidad a la cuenta si el titular es valido. La cuenta puede estar en números rojos.
- mostrar() que ahora debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

'''

from CuentaJoven import *
from Persona import *

persona1 = Persona("Andrea", "Contreras", 27, 1)

cuenta = CuentaJoven(persona1, 20, 5)

cuenta.mostrar()
print(cuenta.esTitularValido())
cuenta.retirar(10)