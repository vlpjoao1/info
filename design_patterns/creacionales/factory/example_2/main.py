from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """El creador declara el metodo Factory que debe retornar un objeto de una clase de producto.
    Las subclases del creador usualmente proporcionan la implementación de este método"""

    @abstractmethod
    def factory_method(self):
        """Tenga en cuenta que el creador puede tambien proveer una implementación predeterminada
         del método factory"""
        pass

    def some_operations(self) -> str:
        """Tenga en cuenta que, a pesar de su nombre, la principal responsabilidad del creador no es
        la creacion de productos. Por lo general, esto contiene la lógica de negocio central que
        se basa en objetos del producto devueltos por el método Factory"""

        # call the factory method to create product object
        product = self.factory_method()

        # Now, use the product
        result = f"Creator: El codigo creador acaba de funcionar con: {product.operation()}"

        return result


"""Los creadores concretos sobreescriben el método factory para cambiar el tipo de producto resultado"""


class ConcreteCreator1(Creator):
    """Tenga en cuenta que la firma del método todavía usa el tipo de producto abstracto,
    a pesar de que el producto concreto en realidad se devuelve del método. De esta forma,
    el creador puede mantenerse independiente de las clases de productos concretos."""

    def factory_method(self) -> IProduct:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):

    def factory_method(self) -> IProduct:
        return ConcreteProduct2()


class IProduct(ABC):
    """La interfaz de producto declara las operaciones que todos los productos concretos
    deben implementar"""
    @abstractmethod
    def operation(self) -> str:
        pass

"""Los productos concretos proporcionan varias implemtaciones de la interfaz de producto"""
class ConcreteProduct1():
    def operation(self) ->str:
        return "{Result of ConcreteProduct1}"


class ConcreteProduct2():
    def operation(self) -> str:
        return "{Result of ConcreteProduct2}"

def client_code(creator: Creator) -> None:
    """El codigo cliente funciona con una instancia de un ConcreteCreator, aunque a traves de su
    interfaz base (creator). Mientras el cliente este trabajando con el creador a traves de la
    interfaz base, puede pasarle cualquier subclase de creador"""

    print(f"Cliente: No estoy al tanto de la clase creadora, pero igual funciono. \n"
          f"{creator.some_operations()}", end="")

if __name__ == "__main__":
    print("App: Ejecutado con el ConcreteCreator1")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Ejecutado con el ConcreteCreator2")
    client_code(ConcreteCreator2())
