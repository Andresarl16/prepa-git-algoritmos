'''
Ejercicio 5.1 

Se le pide que cree un algoritmo que permita el registro de personas. 
Debe guardar cada persona registrada en una lista, tambien se le solicita que use clases. 
La informacion que se desea guardar es el nombre, apellido, edad y DNI de cada persona que se registre en el sistema.

Requerimientos

- Usar clases.
- Usar una lista para guardar la informacion.
- Crear un metodo mostrar() que imprima toda la informacion de la persona.
- Crear un metodo esMayor() que retorne verdadero si la persona tiene 18 años o mas y que retorne falso en caso contrario.

'''

from Registro import *
from Persona import *

registro = Registro()

persona1 = Persona("Andrea", "Contreras", 27, 1)
persona2 = Persona("Andres", "Gomez", 24, 2)

registro.agregarPersona(persona1)
registro.agregarPersona(persona2)
registro.mostrar()
print(persona1.esMayor())

