"""
Ejemplo de Clases:

Clase Camisetas:

Camiseta1: Marca: Nike | Talla: M | Precio 20.00
Camiseta2: Marca: Gucci| Talla: L | Precio 799.99
Camiseta3: Marca: Adidas|Talla: S | Precio 25.00

"""


# Creación de una clase con Python. Simplemente "class" + nombre de la clase + :
class Camiseta:
# Atributos
    talla = "XL"
    color = "rojo"
    precio = 19.99
    marca = "KevorIndustries"


# Creación de nuestra primera instancia de la clase "Camiseta"
# Instanciamos en una variable un objeto de la clase "Camiseta" simplemente llamando la clase:


camisetaSpiderman = Camiseta()  # Llamar a la clase (por su nombre tal cual) con Mayúscula! 


# Acceso a los atributos (talla, color, etc.) de la clase ("Camiseta")
# Accedemos con la nomenclatura del PUNTO!:

camisetaSpiderman.talla
camisetaSpiderman.color
camisetaSpiderman.precio
camisetaSpiderman.marca

# NOTA: La nomenclatura del punto también sirve para llamar a los Métodos
# Los atributos se llaman desde UN OBJETO O INSTANCIA de la clase!!!


# Imprimimos los atributos de nuestra primera instancia u objeto:
# (con un poco de formato)

print(camisetaSpiderman.talla)

print("Talla de la camiseta: " + camisetaSpiderman.talla)
print("Color de la camiseta: " + camisetaSpiderman.color)
print("Precio de la camiseta: " + str(camisetaSpiderman.precio))
print("Marca de la camiseta: " + camisetaSpiderman.marca)




print()
print()
print()


# METODO __INIT__

# Cuando instanciamos (creamos un objeto) de una clase, el método __init__ se ejecuta por defecto en Python.
# Al instanciar un objeto, por ejemplo:

# camisetaPunk = Camiseta()

# Automaticamente se ejecuta el metodo __init__ 
# Este método lo tenemod que DEFINIR NOSOTROS MISMOS dentro de la clase:

# DEFINICIÓN DEL METODO __init__

class Camiseta:
    def __init__(self):     # __init__ SIEMPRE lleva el parámetro SELF!
        pass






















