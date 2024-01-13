# Variables
print(20+20)
print("hola")
camina = True

food = 10
total = food + 5
#print(total)

print("el total es: ",total)
print(f'')

# if
print("\n--------IF--------\n")

if total == 10:
    print("el total es 10")
if total < 10:
    print("el total es menor que 10\n")
if total > 10:
    print("el total es mayor que 10")
    print( "ganaste")

else:
    print("error")

contador = 0

if contador == 0:
    print(contador)
    contador = contador + 1
    if contador == 1:
        print(contador)
        contador = contador+1
        if contador == 2:
            print(contador)
            contador = contador+1

# for
            
print("\n--------FOR--------\n")

contador2 = 1
for i in range(1,10,2):
    print(i, contador2)
    contador2 +=1

for i in range(1,6):
    print (i, 5*(i))

opcion = 0 #int(input("elija un numero"))
if opcion == 1:
    for i in range(0,11):
        print(i,1*i)
if opcion == 2:
    for i in range(0,11):
        print(i,2*i)

print("\n--------WHILE--------\n")

dia = 0 
semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
while dia < 7:
   print("Hoy es " + semana[dia])
   dia += 1

print("\n--------Switch--------\n") # no existe en python
#switch (opcion)
#    case 1 :
#        menu1

print("\n--------Lista--------\n")
lista = [15,20,78,14,3,9]
print(lista[1])


print("\n--------Función--------\n")
def funcion(x, y):
    resultado = (2*x)+(5*y)

    print(resultado) 

#valorX = int(input("valor x: "))
#valorY = int(input("valor y: "))

#funcion(valorX,valorY)

print("\n--------Arreglos--------\n")

Array = []

for i in range(10):
    multi = i*5
    Array.append(multi) # añade el valor al arreglo
    

    print("5 x", i, "=", Array[i])

print(Array)
Array.pop() # Elimina el último
print(Array)
Array.remove(10) # elimina el número elegido
print(Array)
Array.insert(0,100) # inserta en la posición , el némero a insertar
print(Array)
Array.sort() # Ordena de menor a mayor
print(Array)

tuple = (5,8,6) # Arreglo diferente

diccionario = {}

animales = {'pajaro':'volador',
            'perro':'tierra',
            'pez':'agua'}

print(animales)
animales.update({'pajaro':'no vuela'}) #Actualiza el dato de la {llave} que se le da
print(animales)


cuenta = [1,4,6,7,5,1,7,3,9]
suma = 0

for i in range(len(cuenta)): # Lee el tamaño
    suma += 1
print(suma)

print(len(cuenta))

Matriz = [{1,2,3},
          {7,8,4}]
print(Matriz)

matriz2 = [{1,2,3},
           {"agua","gaseosa","jugo"}]
print(matriz2)

print("\n--------------------\n")
peliculas = [["avengers",2,2012,"robert"],
             ["wakanda", 1,2017, " chadwick"]]
duracion = []

for i in range(len(peliculas)):
    dur = peliculas[i][1]
    duracion.append(dur)
print(duracion)