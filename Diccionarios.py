diccio={"Alemania":"Berlín","Argentina":"Bs As","Suzia":"Berna"}
print(diccio["Argentina"])
print(diccio)

'añadir un elemento'
diccio["Italia"]="París"
print(diccio)
print("...")

'modificar elementos, es simple y sobreescribe'
diccio["Italia"]="Roma"
print(diccio)
print("...")

'eliminar elementos'
del diccio["Alemania"]
print(diccio)
print("...")


diccio2={"hola":"chau", 10:"messi", "CR7":7}
print(diccio2)
print("...")

tupla=["Alemania","Argentina","Suzia","Italia"]
diccio3={tupla[0]:"Europa",tupla[1]:"América",tupla[2]:"Asia"}
print(diccio3)
print("...")

diccio4={10:"Lionel",5:"Masche","DTS":{"camisetas":[1, 2, 3, 4]}}
print(diccio4)
print(diccio4["DTS"])
print("...")
print("...")


print(diccio4.keys())
print(diccio4.values())
print(len(diccio4))


