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

# El método __init__ inicializa (construye) un objeto
# Aquí pondremos los valores de los atributos de nuestro objeto y al instanciarlo
# se creará con dichos atributos

# INIT CREA INSTANCIAS CON VALORES Y ATRIBUTOS INICIALES

# SELF -> Una referencia a la instancia actual de la clase.
"""
self.color = 'rojo'
self.marca = 'Puma'
self.precio = 29.99
"""

# Al instanciar el objeto e inicializarlo con los valores de los atributos predefinidos (gracias a __init__)
# self pasa a ser la referencia de dicho objeto, por ejemplo:

camisetaPunk = Camiseta()

# self es la referencia de la instancia actual, es decir, "camisetaPunk"

#self.color 
camisetaPunk.color # output: rojo

#self.marca
camisetaPunk.marca # output: Puma

#self.precio
camisetaPunk.precio # output: 29.99


# Código de la explicación anterior limpio:
# Creación de una clase con su objeto constructor __init__

class Camiseta:
    def __init__(self):
        # Atributos con los que se inicializará la instancia (objeto) creado de esta clase
        self.marca = "Gucci"
        self.precio = 99.99
        self.talla = "M"
        self.color = "negro"
    
# Al instanciar un objeto, se incializará con estos valores pre-definidos

# camisetaRosa = Camiseta()


# USO Y CREACIÓN CORRECTA DE CLASES CON INIT

# Lo que debemos hacer al inicilizar una clase con el método init es
# PASAR LOS ATRIBUTOS como PARAMETROS del mismo método init, así:

class Camiseta:
    def __init__(self, marca, precio, talla, color): # Parámetros de la clase en el método init para inicializar objetos con estos atributos por defecto!


# Ya pasados como parámetros del método init los atributos de nuestra instancia simplemente
# los asignamos a lo que pasemos como argumento al llamar a la clase:

        self.marca = marca
        self.precio = precio
        self.talla = talla
        self.color = color

# Ahora, al crear el objeto, simplemente le pasamos el VALOR de sus atributos
# como parámetros al crear la instancia, por ejemplo:

# Atributos del objeto instanciado marca, precio, talla, color

camisetaAnime = Camiseta("Nike", 19.99, "S", "Azul") # Pasamos el VALOR del atributo


# Ahora, ya podemos crear todas las camisetas (objetos) que queramos :D
camisetaVerde = Camiseta("Nike", 19.99, "S", "Verde")
camisetaBlanca = Camiseta("Adidas", 19.99, "XL", "Blanca")
camisetaRoja = Camiseta("Puma", 19.99, "L", "Roja")



# Creación de un MÉTODO de una CLASE (es como una función)

# Supongamos que necesitamos aplicar un descuento a ciertas camisetas, por lo tanto
# vamos a crear un método que haga eso:

# ABAJO ANEXO CÓDIGO LIMPIO, TOMAR EN CUENTA LA INDENTACION!!!!!!!!!!!!!!!!!!

# Este método recibe un parámetro (aparte de self) que será el porcentaje a descontar
# Y luego calcula dicho descuento y lo aplica al precio original de la camiseta

    def aplicarDescuento(self, porcentaje):     # SIEMPRE LLEVA SELF CUANDO HABLAMOS DE POO!!
        self.precio = self.precio*porcentaje/100 # Si introducimos 20 se hará un descuento del 20% al precio original

# Para llamar este método a una instancia usamos igual la NOMENCLATURA DEL PUNTO!:

print(camisetaAnime.precio)     # Antes de aplicar el descuento
camisetaAnime.aplicarDescuento(50)
print(camisetaAnime.precio)     # Después de aplicar el descuento


# Vamos a agregar un nuevo atributo a la clase Camiseta, que será un Booleano
# que nos indicará si el producto esta ya con descuento o no

self.rebaja = False # Inicialmente el atributo estará inicializado en False (NO VA COMO PARAMETRO EN EL METODO INIT)


# Si a la camiseta se le aplica un descuento, entonces esta pasa a estar rebajada,
# por lo tanto, debemos cambiar el False de self.rebaja a True.

# Dentro de nuestro método "aplicarDescuento" vamos a VERIFICAR que el porcentaje
# que nos pasen no sea mayor de 100 (no podemos vender algo a 120% de descuento verdad?)

if porcentaje < 100:        # Si el porcentaje es menor del 100%, osea,  tiene rebaja
    self.rebaja = True      # Entonces, efectivamente tiene rebaja, osea, TRUE.




# Implementación de un método que nos muestre toda la información del producto.
# Simplemente haremos un método que muestre la información (los atributos) del producto.

def infoProducto(self):
    print("Descripción del producto:")
    info = f"Marca: {self.marca}\nPrecio: {self.precio}\nTalla: {self.talla}\nColor: {self.color}"

# Comprobamos si el producto tiene rebaja, si sí (True) a la info le concatenamos
#el mensaje de que tiene descuento

    if self.rebaja == True:
        info += "PRODUCTO CON DESCUENTO"
    return info
