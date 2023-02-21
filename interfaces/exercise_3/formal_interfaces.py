"""Otra forma de crear interfaces es con clases abstractas
Al usarlas se resuelven algunos de los problemas que se dan
cuando se udan interfaces informmales."""

"""Creamos la interfaz al crear una clase que hereda de ABC,
el decorador abstractmethod es usado para los metodos"""

"""Con esta tecnica obtendremos:
- Mayor claridad, se notara que no es una clase comun
- Al ser abstracta, desde luego se debe de implementar
- Si no implementamos un metodo, se levanta una excepcion
- Si intentamos instanciar obtenemos una excepcion"""

# La desventaja es que es muy general, no sabemos si la clase es una interfaz u otra cosa

from abc import ABC, abstractmethod


class IAnimal(ABC):
    """ Esta es la clase que define la interfaz IAnimal"""

    @abstractmethod
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

    @abstractmethod
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


# para usar la interfaz hacemos herencia y override a los metodos para crear su implementacion

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


##

class Perro(IAnimal):

    # solo implementaremos uno de los dos metodos
    def caminar(self, metros: int):
        if metros > 70 and metros < 850:
            print('Tu perro esta caminando lo suficiente')
        else:
            print('Vigila cuanto camina tu perro')


miPerro = Perro()

## intentamos instanciar directamente

miOtroGato = IAnimal()
