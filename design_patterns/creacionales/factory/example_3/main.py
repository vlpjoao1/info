from __future__ import annotations
from abc import ABC, abstractmethod


# Creator
"""Interfaz de IEnemyCreator"""
class IEnemyCreator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operations(self, vida: int, resistencia: int, nivel: int) -> str:
        enemy = self.factory_method(vida=vida, resistencia=resistencia, nivel=nivel)
        result = f'Creador: Se ha generado un enemigo llamado: {enemy.operations()}'
        return result


class JalatoCreator(IEnemyCreator):

    def factory_method(self, vida: int, resistencia: int, nivel: int) -> IEnemy:
        return Jalato(vida=vida, resistencia=resistencia, nivel=nivel)


# Products
class IEnemy(ABC):

    def __init__(self, vida: int, resistencia: int, nivel: int) -> None:
        self.vida = vida
        self.resistencia = resistencia
        self.nivel = nivel

    @abstractmethod
    def operations(self) -> str:
        pass


class Jalato(IEnemy):

    def operations(self) -> str:
        return f'Jalato.  vida:{self.vida}, resistencia:{self.resistencia}, nivel:{self.nivel}'


def client_code(creator: IEnemyCreator, vida, resistencia, nivel) -> None:
    print(creator.some_operations(vida=vida, resistencia=resistencia, nivel=nivel))


if __name__ == '__main__':
    client_code(JalatoCreator(), vida=100, resistencia=200, nivel=10)
    client_code(JalatoCreator(), vida=200, resistencia=400, nivel=20)
