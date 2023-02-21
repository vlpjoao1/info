from __future__ import annotations
from abc import ABC, abstractmethod


# Factory
class IAbstractFactory(ABC):
    """La fabrica abstracta declara un grupo de metodos que retorna
    diferentes productos abstractos. Estos productos son llamados
    una familia y estan relacionados por un concepto de alto nivel.
    Los productos de una familias son capaces de colaborar entre ellos.
    Una familia de productos puede tener muchas variantes, pero los
    productos de una variante son incompatibles con productos de otra.

    """

    @abstractmethod
    def create_product_a(self) -> IAbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> IAbstractProductB:
        pass


class ConcreteFactory1(IAbstractFactory):
    """Las fabricas concretas producen una familia de productos que
    que pertenecen a una variante simple. La fabrica garantiza que los
    productos resultantes son compatibles. Ten en cuenta que las
    firmas de las fabricas conretas retornan un producto abstracto, mientras
    que dentro del metodo un producto concreto es instanciado."""

    def create_product_a(self) -> IAbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> IAbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(IAbstractFactory):
    """Cada fabrica concreta tiene una correspondencia a una
    variante de producto."""

    def create_product_a(self) -> IAbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> IAbstractProductB:
        return ConcreteProductB2()


# products
class IAbstractProductA(ABC):  # Product A
    """Cada producti distinto de una familia de productos debe tener
    una interfaz base"""

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""Los productos concretos son creados para corresponder a una fabrica
concreta"""


class ConcreteProductA1(IAbstractProductA):
    def useful_function_a(self) -> str:
        return "El resultado de producto A1"


class ConcreteProductA2(IAbstractProductA):
    def useful_function_a(self) -> str:
        return "El resultado de producto A2"


class IAbstractProductB(ABC):  # Produc B
    @abstractmethod
    def useful_function_b(self) -> None:
        """Producto B puede hacer sus cosas"""
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: IAbstractProductA) -> None:
        """Tambien puede colaborar con otro producto

        La fabrica abstracta se asegura de que todos los productos que crea
        sean de la misma variante y por lo tanto, compatibles
        """
        pass


class ConcreteProductB1(IAbstractProductB):
    def useful_function_b(self) -> str:
        return "El resultado de producto B1"

    def another_useful_function_b(self, collaborator: IAbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"El resultado de B1 colaborando con el ({result})"


class ConcreteProductB2(IAbstractProductB):
    def useful_function_b(self) -> str:
        return "El resultado de Producto B2"

    def another_useful_function_b(self, collaborator: IAbstractProductA) -> str:
        """La variante, producto B2,solo puede funcionar con el variante,
        Producto A2. Sin embargo, acepta cualquier instance de
        AbstractProductA como argumento"""
        result = collaborator.useful_function_a()
        return f"El resultado de B2 colaborando con el ({result})"


def client_code(factory: IAbstractFactory) -> None:
   """El codigo cliente trabaja con factorys y productos solo a traves de
   los tipos abstractos:AbstractFactory y AbstractProduct. Esto
   te deja pasar alguna subclase de fabrica o producto al codigo cliente
   sin romperlo."""
   product_a = factory.create_product_a()
   product_b = factory.create_product_b()

   print(f"{product_b.useful_function_b()}")
   print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """El codigo cliente puede trabajar con cualquier
    fabrica concreta"""

    print("Client: Probando el codigo cliente con el primer tipo de fabrica:")
    client_code(ConcreteFactory1())
    print("\n")

    print("Client: Probando el codigo cliente con el segundo tipo de fabrica:")
    client_code(ConcreteFactory2())