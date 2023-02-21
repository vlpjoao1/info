#El duck typing se fundamente en el razonamiento inductivo.
#donde una serie de premisas apoyan la conclusión, pero no la garantizan.
"""A python le dan igual los tipos de los objetos,lo
unico que le importan son sus metodos."""
class Perro:
    def hablar(self):
        print("¡Guau, Guau!")

class Gato:
    def hablar(self):
        print("¡Miau, Miau!")

class Vaca:
    def hablar(self):
        print("¡Muuu, Muuu!")

"""Como podemos observar, en Python no es necesario
especificar los tipos, simplemente decimos que el parametro
de entrada tiene nombre X."""
#1er form
def llama_hablar(x):
    x.hablar()
llama_hablar(Perro())
llama_hablar(Gato())
llama_hablar(Vaca())

#2da form
lista = [Perro(), Gato(), Vaca()]
for animal in lista:
    animal.hablar()
