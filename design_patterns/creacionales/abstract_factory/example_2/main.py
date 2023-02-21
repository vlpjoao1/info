"""Situacion:
-Tenemos 3 tipos de enemigos: Aereos, Terrestres y Acuáticos
-Tenemos 3 familias de enemigos: Jalato, Jalamut y Wabbit.
Necesitamos crear fabricas para cada familia, que produzca los 3
tipos de enemigos.
Usando Abstract Factory."""

# --------------------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod


class IEnemyFactory(ABC):  # Enemy interface

    @abstractmethod
    def generate_flying_enemy(self) -> IFlyingEnemy:
        pass

    @abstractmethod
    def generate_ground_enemy(self) -> IGroundEnemy:
        pass

    @abstractmethod
    def generate_aquatic_enemy(self) -> IAquaticEnemy:
        pass


class JalatoFactory(IEnemyFactory):

    def generate_flying_enemy(self) -> IFlyingEnemy:
        return FlyingJalato()

    def generate_ground_enemy(self) -> IGroundEnemy:
        return GroundJalato()

    def generate_aquatic_enemy(self) -> IAquaticEnemy:
        return AquaticJalato()


class JalamutFactory(IEnemyFactory):

    def generate_flying_enemy(self) -> IFlyingEnemy:
        return FlyingJalamut()

    def generate_ground_enemy(self) -> IGroundEnemy:
        return GroundJalamut()

    def generate_aquatic_enemy(self) -> IAquaticEnemy:
        return AquaticJalamut()


class WabbitFactory(IEnemyFactory):

    def generate_flying_enemy(self) -> IFlyingEnemy:
        return FlyingWabbit()

    def generate_ground_enemy(self) -> IGroundEnemy:
        return GroundWabbit()

    def generate_aquatic_enemy(self) -> IAquaticEnemy:
        return AquaticWabbit()


# Products
##Flying Enemys
class IFlyingEnemy(ABC):

    @abstractmethod
    def generate_enemy(self) -> None:
        pass


class FlyingJalato(IFlyingEnemy):

    def generate_enemy(self) -> str:
        return "Jalato Volador"


class FlyingJalamut(IFlyingEnemy):

    def generate_enemy(self) -> str:
        return "Jalamut Volador"


class FlyingWabbit(IFlyingEnemy):

    def generate_enemy(self) -> str:
        return "Wabbit Volador"

##Ground Enemys
class IGroundEnemy(ABC):

    @abstractmethod
    def generate_enemy(self)->None:
        pass

class GroundJalato(IGroundEnemy):

    def generate_enemy(self) ->str:
        return "Jalato Terrestre"

class GroundJalamut(IGroundEnemy):

    def generate_enemy(self) ->str:
        return "Jalamut Terrestre"

class GroundWabbit(IGroundEnemy):
    def generate_enemy(self) ->str:
        return "Wabbit terrestre"

##Aquatic Enemys
class IAquaticEnemy(ABC):

    @abstractmethod
    def generate_enemy(self)->None:
        pass

class AquaticJalato(IAquaticEnemy):

    def generate_enemy(self) ->str:
        return "Jalato Acuatico"

class AquaticJalamut(IAquaticEnemy):

    def generate_enemy(self) ->str:
        return "Jalamut Acuatico"

class AquaticWabbit(IAquaticEnemy):

    def generate_enemy(self) ->str:
        return "Wabbit Acuatico"

# Client Code

def client_code(factory : IEnemyFactory) -> None:
    ground_enemy=factory.generate_ground_enemy()
    flying_enemy=factory.generate_flying_enemy()
    aquatic_enemy=factory.generate_aquatic_enemy()

    print("Probando codigo cliente: \n")
    print(f"{ground_enemy.generate_enemy()}")
    print(f"{flying_enemy.generate_enemy()}")
    print(f"{aquatic_enemy.generate_enemy()}")

if __name__ == "__main__":
    """El codigo cliente trabaja con cualquier fabrica concreta"""
    client_code(WabbitFactory())

