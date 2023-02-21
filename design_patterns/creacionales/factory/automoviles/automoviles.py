class Automovil(object):
    def __init__(self, marca: str):
        self.marca = marca
        self.__estado = 0

    def arrancar(self) -> None:
        if self.__estado == 0:
            print("Arrancando el auto ", self.marca)
            self.__estado = 1
        else:
            print("El auto ", self.marca, " no ha arrancado")

    def detener(self):
        if self.__estado == 1:
            print("Deteniendo el auto ", self.marca)
            self.__estado = 0
        else:
            print("El auto ", self.marca, " no ha arrancado")

    def nitro(self):
        print("Aplicando Nitro auto deportivo")


class AutomovilDeportivo(Automovil):
    def __init__(self, marca):
        super(AutomovilDeportivo, self).__init__(marca)
        print("Has adquirido un automovil deportivo marca", self.marca)


class AutomovilFamiliar(Automovil):
    def __init__(self, marca):
        super(AutomovilFamiliar, self).__init__(marca)
        print("Has adquirido un automovil familiar marca", self.marca)

    def nitro(self):
        print("El automovil familiar carece de nitro")
