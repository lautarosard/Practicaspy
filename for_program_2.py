#Bucle For
print("Bucle for/practica")

viajes=[["Parana",1],["Entre Rios",2],["San Luis",32],["Merlo",8],["Cordoba",5],["Tandil",6]]
dest_nuev=str(input("Ingrese el nuevo destino: "))
num_nuev=int(input("Ingrese un nuevo num: "))
listnuviaje=[dest_nuev,num_nuev]
viajes.append(listnuviaje)
for dato in viajes:
    print(dato)
print("-"*50)
viajes.remove(viajes[3])
for dato in viajes:
    print(dato)