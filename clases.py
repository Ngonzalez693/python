# Clases

class Persona(): # Definición clase

    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre # Variables
        self.edad = edad
    
    def hablar(self): # Métodos
        print(f" mi nombre: {self.nombre}, edad: {self.edad}")

persona1 = Persona("juan","20") # Crear objeto
persona1.hablar()

class Estudiante(Persona): # Herencia

    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad) # Hereda los atributos
        self.carrera = carrera

    def intro(self):
        print(f"mi nombre es {self.nombre} y estudio {self.carrera}")

estudiante1 = Estudiante("jose","25","derecho")
estudiante1.intro()
estudiante1.hablar() # hereda los métodos

print("\n---------------------\n")

# Polimorfismo

class Animal():
    def sonido(self): # Método original
        pass

class Perro(Animal):
    def sonido(self): # Variaciones del metodo
        return "guau"
    
class Gato(Animal):
    def sonido(self): # Variaciones del metodo
        return "miau"

def sonarRuido(animal): # Distribución de cual método se usa
    return animal.sonido()

perro = Perro()
gato = Gato()

print(sonarRuido(perro))
print(sonarRuido(gato))

print("\n---------------------\n")

# get y set
class Cantante():
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre
        
    def getGenero(self):
        return self.genero
    
    def setGenero(self, nuevoGenero):
        self.genero = nuevoGenero

Cantante1 = Cantante("luis", "rock")
Cantante2 = Cantante("jose", "pop")
Cantante3 = Cantante("juan", "rap")
Cantante4 = Cantante("maria", "trap")
Cantante5 = Cantante("luisa", "rock")

print(Cantante1.getNombre())
print(Cantante1.getGenero())

#print(Cantante1.setNombre("Rob"))
#print(Cantante1.setNombre("pop"))

#print(Cantante1.getNombre())
#print(Cantante1.getGenero())

print("\n---------------------\n")

cantantes = [Cantante1, Cantante2, Cantante3, Cantante4, Cantante5]

for i in range(len(cantantes)):
    print(cantantes[i].getNombre(),cantantes[i].getGenero())
