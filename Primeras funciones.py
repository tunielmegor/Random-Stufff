def mensajeanding():
	print("hola")
	print("chau")
	'esta es la definición de la función, '''
	'que luego la llamamos a ejecutarse'''
	'Hay que recordar las indentadas o sangrías o tabulaciones'''
	'esta no recibe ningún parámetro. La de suma estaría recibiendo 2'

mensajeanding()
print("!!!!!cortando!!!!!!")
mensajeanding()




def sumanding(num1, num2):
	print(num1+num2)

sumanding(5,7)
sumanding(2.57,0.135)
'acá recibe 2 parámetros, que los definimos en cada llamada'

def sumanding2(nro1, nro2):
	resultado=nro1+nro2
	return resultado

print(sumanding2(6, 8))
print(sumanding2(3, 4))

almacenamiento=sumanding2(9,11)
print(almacenamiento)
'definimos la variable con el valor resultado o retorno de la función sumanding'
print("caca")
