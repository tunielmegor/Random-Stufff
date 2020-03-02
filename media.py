cantidad = int(input("Tamaño de la muestra: "))
total = 0
lista = []
nro_menos_mediaacum = 0

for i in range(cantidad):
    nro = float(input("Ingrese valores uno a uno "))
    lista.append(nro)
    total = total + nro
    #total += float(nro)

media=total/cantidad
print("media = "media)

for i in range(cantidad):
    temporal = lista[i]
    nro_menos_media = (temporal - media) ** 2
    nro_menos_mediaacum = nro_menos_mediaacum + nro_menos_media

desvest=nro_menos_mediaacum/media
print("resultado final= "desvest)
