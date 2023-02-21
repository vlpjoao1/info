# Example 1 ----------------------------------
# Using abd.ABCmeta
"""Para hacer cumplir que las subclases instancien
los metodos abstractos puedes usar el modulo ABC"""
import abc

"""De esta forma en vez de sobreescribir los dunder methods
.__instancecheck__() y __subclasscheck__() solo sobreescribiremos
.__subclasshook__()"""


class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and callable(subclass.load_data_source)
                and hasattr(subclass, 'extract_text') and callable(subclass.extract_text))


class PdfParserNew:
    """Extract text from a PDF."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass


class EmlParserNew:
    """Extract text from an email."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass


print(issubclass(PdfParserNew, FormalParserInterface))
print(issubclass(EmlParserNew, FormalParserInterface))

print('-' * 50)
# Example 2 ------------------------------------------------
# Usando ABD para registrar una subclase

"""De esta forma registramos una clase virtual a Double"""


class Double(metaclass=abc.ABCMeta):
    """Double precision floating point number."""
    pass


"""Registramos la clase flotante como subclase de Double"""
Double.register(float)
print(issubclass(float, Double))  # True
# isinstance ya que al ser un numero para a ser una instancia de float
print(isinstance(1.2, Double))  # True

"""Puedes usar los decoradores para registrar"""


@Double.register
class Double64:
    """A 64-bit double-precision floating-point number."""
    pass


print(issubclass(Double64, Double))  # True


# Example 3 ----------------------------
# Usando la deteccion de subclases con registro

class FormalParserInterface2(metaclass=abc.ABCMeta):
    @classmethod
    def __subclassook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and callable(subclass.extract_text)
                or NotImplemented)
