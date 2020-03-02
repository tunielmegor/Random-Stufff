tupla1=("tuni",26,5,1996)
print(tupla1[0])
lista=list(tupla1)
'construí una lista de la tupla'
print(lista)
print(lista[:])

'para hacer tuplas de listas, es igual pero el comando es tuple'
tuplaes=tuple(lista)
print(tuplaes)

print("tuni" in tupla1)
print("tunisia" in tupla1)

print("...")

'contar elementos en una tupla'
print(tupla1.count(1996))

'el método len permite averiguar la longitud de una tupla'
print(len(tupla1))
'ojo de confundir la cantidad con el ínidce'

tupla2="carlos",12,4,1998
'sin paréntesis'
print(tupla2)
print("...")

'empaquetados y desempaquetados de tuplas'

nombre, dia, mes, año=tupla2

print(mes)
print(año)
print(nombre)
print(dia)
print("...")

'si se permite el index, pero no permite remove, append, extend'
