from factory import FactoryAutomovil


def main():
    auto1 = FactoryAutomovil.get_automovil("Deportivo", "Toyota")
    auto2 = FactoryAutomovil.get_automovil("Familiar", "Hyundai")
    auto1.nitro()
    auto2.nitro()

main()
