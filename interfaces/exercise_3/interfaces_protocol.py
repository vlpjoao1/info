# Protocol

# Es una opcion nueva que viene con el PEP544 en Python 3.8
# Es una forma implicita de declarar interfaces
# Solo es de ayuda si hacemos  uso de type hints y verificacion estatica de tipos

from typing import Protocol


class IAnimal(Protocol):
    """ Esta es la clase que define la interfaz IAnimal"""

    # type hints = nombre:str
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


# Para la implementacion debemos de seguir con el protocolo de tipos

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
