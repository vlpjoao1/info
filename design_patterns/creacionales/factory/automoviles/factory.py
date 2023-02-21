from automoviles import AutomovilDeportivo, AutomovilFamiliar


class FactoryAutomovil:
    @staticmethod
    def get_automovil(tipo, marca):
        if tipo == "Deportivo":
            return AutomovilDeportivo(marca)
        elif tipo == "Familiar":
            return AutomovilFamiliar(marca)
        else:
            return "Tipo invalido"
