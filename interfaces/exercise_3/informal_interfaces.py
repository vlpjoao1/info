# Existen distintas formas de declarar interfaces
# Informal
# Por clases abstractas
# Protocol

"""Las interfaces nos permiten aislar la logica central de las dependencias externas."""


###INFORMAL ###
# Esta tecnica se crea usando una clase normal

# Los metodos no se implementan, solo se colocan las annotations y el docstring
# docstring = documentacino, annotations=tipos de valores esperados
class IAnimal:
    """Esta es la clase que define la interfaz animal"""

    def colocadatos(self, nombre: str, peso: float) -> bool:
        """
        Parameters
        -----------
        nombre : str
            nombre del animal
        peso : float
            Peso del animal
        Returns
        ----------
        IAnimal
            Indico si el animal tiene sobrepeso
        """

    def caminar(self, metros: int):
        """
        Parameters
        -----------
        metros:int
            Cantidad minima que camina
        Returns
        ----------
        None.
        """


"""Las clases que van a implementar dichas intefaces, son las que tendran la responsabilidad
de la forma como esos metodos deben de actuar, tienen la responsabilidad de llevar a cabo
la implementacion"""

"""Para usar la interfaz necesitamos hacer una herencia y override a los metodos, para crear
su implementacion"""


class Gato(IAnimal):
    def colocadatos(self, nombre: str, peso: float) -> bool:
        self.nombre = nombre
        self.peso = peso
        if self.peso > 7:
            return True
        else:
            return False

    def caminar(self, metros: int):
        if metros > 70 and metros < 850:
            print("Tu gato camina lo suficiente")
        else:
            print("Vigila cuanto camina tu gato")

    # Forma e representar un objeto como string
    def __repr__(self):
        return f'Tu gato {self.nombre} pesa {self.peso} Kg'


miGato = Gato()

print(miGato.colocadatos('Gatito', 6.5))
miGato.caminar(350)
print(miGato)

"""Una desventaja de las interfaces informales es que pueden haber clases que no
implementen la interfaz por lo que no hay una garantia de que la interfaz es
implementada

Estos metodos retornaran None
"""


class Perro(IAnimal):
    pass


miPerro = Perro()
print(miPerro.colocadatos('Lomito', 12))


# Para solucionar este error debemos levantar una excepcion de NotImplementedError

class IAnimal2:
    """Esta es la clase que define la interfaz animal"""

    def colocadatos(self, nombre: str, peso: float) -> bool:
        """
        Parameters
        -----------
        nombre : str
            nombre del animal
        peso : float
            Peso del animal
        Returns
        ----------
        IAnimal
            Indico si el animal tiene sobrepeso
        """
        raise NotImplementedError

    def caminar(self, metros: int):
        """
        Parameters
        -----------
        metros:int
            Cantidad minima que camina
        Returns
        ----------
        None.
        """
        raise NotImplementedError


class Tortuga(IAnimal2):
    pass

miTortuga=Tortuga()
print(miTortuga.colocadatos('Leo',0.24))

#otra desventaja es que podemos instanciar la interfaz como si fuera una clase normal
miInstancia = IAnimal()