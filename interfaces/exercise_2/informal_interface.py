""" https://realpython.com/python-interface/#informal-interfaces
Las interfaces informales permiten a las clases implementen de forma
no estricta la interfaz, esto quiere decir que estas interfaces
definen metodos que pueden ser sobreescritos.
"""


class InformalParserInterface:
    def load_data_source(self, path: str, filename: str) -> str:
        """Load in the file for extracting here"""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file"""
        pass


class PdfParser(InformalParserInterface):
    """Extract text from a pdf"""

    def load_data_source(self, path: str, filename: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        pass


"""EmlParser no implementa correctamente la <<interfaz>>
debido a que no se define correctamente .extract_tect()"""


class EmlParser(InformalParserInterface):
    """Extract text from an email"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        pass


# El ORM te mostrara el orden en el que se buscan para
# ejecutar os metodos
print(PdfParser.__mro__)
print(EmlParser.__mro__)

print(issubclass(PdfParser, InformalParserInterface))
"""Esta ultima devolvera True, lo que es un problema
 ya viola la definicion de interfaces"""
print(issubclass(EmlParser, InformalParserInterface))

# Example 2 ---------------------------------------------------
## Using metaclass to define informal interface
"""Ya que el metodo issubclass retornara TRUE, lo que viola
la definicion de interfaces, crearemos una metaclase y 
reescribiremos dos dunder methods."""


class ParserMeta(type):
    """A Parser Metaclass that will be user for parser class creation"""

    def __instancecheck__(self, instance):
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        # callable verifica si algo es llamable, es decir si se comporta como una funcion o clase
        return (hasattr(subclass, 'load_data_source') and callable(subclass.load_data_source)
                and hasattr(subclass, 'extract_text') and callable(subclass.extract_text))


class UpdateInformalParserInterface(metaclass=ParserMeta):
    """This interface is used for concrete classes to inherit from.
        There is no need to define the ParserMeta methods as any class
        as they are implicitly made available via .__subclasscheck__().
    """
    pass


class PdfParserNew:
    """Extract text from PDF"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdateInformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> str:
        """Overrides UpdatedInformalParserInterface.extract_text()"""
        pass


class EmlParserNew:
    """Extract text from an email."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override UpdatedInformalParserInterface.extract_text()
        """
        pass


print(issubclass(PdfParserNew, UpdateInformalParserInterface))
"""Como se esperaba, EmlParserNew no es una subclase de UpdateInformalParserInterface
ya que .extract_tect() no fue definido en EmlParserNew"""
print(issubclass(EmlParserNew, UpdateInformalParserInterface))

"""UpdateInformalParserInterface is a superclass of PdfParserNew, but it
doesn't appear in the MRO. Esto es causado por el hecho de que UpdateInformalParserInterface
es una clase base virtual de PdfParserNew"""
print(PdfParserNew.__mro__)
# thats not a subclass of UpdateInformparParserInterface
print(EmlParserNew.__mro__)


# Example 3 --------------------------------------------------------------
## Using Virtual Base Class to define informal interfaces.

class PersonMeta(type):
    """A person metaclass"""

    def __instancecheck__(self, instance):
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        return (hasattr(subclass, 'name') and callable(subclass.age)
                and hasattr(subclass, 'age') and callable(subclass.age))


class PersonSuper:
    """A person superclass"""

    def name(self) -> str:
        pass

    def age(self) -> str:
        pass


class Person(metaclass=PersonMeta):
    """Person interface built from PersonMeta metaclass"""
    pass


# Inheriting subclasses
class Employee(PersonSuper):
    """Inherits from PersonSuper
    PersonSuper will appear in Employee.__mro__"""
    pass


"""A pesar de que Friend no tiene una herencia explicita de Person,
este implementa .name() y .age(), lo que convierte a Fiend en
una Virtual Base Class de Friend."""
class Friend:
    """Construido explicitamente a partir de Person,
    Friend es una subclase virtual de Person ya que ambos
    requieren metodos existentes.
    Person not in Friend.__mro__-"""

    def name(self):
        pass

    def age(self):
        pass

print(issubclass(Friend, PersonSuper))