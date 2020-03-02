milista=["juan", "tuni", "ana","pedro","gaby","fran"]
print(milista[:])
print(milista[0])
print(milista[3])
print(milista[-1])
'es en el orden inverso de la lista'
'ahora vemos la porción de la lista'

print(milista[0:3])
print(milista[4:])

'agregar elementos al final de la lista:'
milista.append("sandra")
print(milista[:])
print("...")

'agregar elementos en cualquier posición'
milista.insert(2,"FEDE")
print(milista[:])
print("...")

'agregar varios elementos'
milista.extend(["facu","luis","belen"])
print(milista[:])
print("...")

print(milista.index("tuni"))
print("...")

'si hay 2 elementos iguales, devuelve el primer elemento'


'Ahora vamos a comprobar si un elemento está en la lista'
print("tuni" in milista) 
'función in'
print("XD"in milista)

'eliminar elementos, con la fucnión remove'
milista.remove("belen")
'recordar que las comillas sólo van porque es texto. Si fueran nros no harían falta'

print(milista[:])
print("...")

'remover el último elemento'
milista.pop()

print(milista[:])
print("...")


milista2=["asdf","fdsa"]*2
'el asterisco es un repetidor'

milista3=milista+milista2

print(milista3[:])
print("...")
 