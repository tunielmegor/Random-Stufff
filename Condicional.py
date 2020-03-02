'''print("Evaluaciones finales")

nota_alumno=input()

def evaluacion(nota):
	valoracion="aprobado"
	if nota<6:
		valoracion="desaprobado"
	return valoracion

print(evaluacion(int(nota_alumno)))



print("Evaluaciones finales")

nota_alumno=input("introducir el resultado: ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<6:
		valoracion="desaprobado"
	return valoracion

print(evaluacion(int(nota_alumno)))'''

'borrar las comillas y ver que el int puede ir en el input o en el print'

'''print("verificación de edad")
edad=int(input("Tu edad: "))

if edad<18:
	print("No pasa")
elif edad>100:
	print("Edad incorrecta")
else:
	print("Pasa")'''

grade=int(input("poné tu nota: "))
if grade<2:
	print("no libre")
elif grade<4:
	print("libre")
elif grade<6:
	print("regular")
elif grade<10:
	print("promoción")
elif grade>10:
	print("nota no válida")
else:
	print("sobresaliente")