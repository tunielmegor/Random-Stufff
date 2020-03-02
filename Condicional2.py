edad=7
if 0<edad<100:
	print("Edad OK")

else:
	print("Edad No OK")


sueldo_presidente=int(input("Introduce sueldo: "))
print("presi $" + str(sueldo_presidente))

'la función int y str transforman en strings y integeres, o enteros, a las variables'

sueldo_vicepresidente=int(input("Introduce sueldo: "))
print("vice $" + str(sueldo_vicepresidente))

sueldo_tuni=int(input("Introduce sueldo: "))
print("tuni $" + str(sueldo_tuni))

sueldo_jefe=int(input("Introduce sueldo: "))
print("jefe $" + str(sueldo_jefe))

if sueldo_presidente>sueldo_vicepresidente>sueldo_tuni>sueldo_jefe:
	print("Todo OK")
else:
	print("Not Ok")

	