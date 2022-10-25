nombre=str(input("Ingrese el tipo del producto: "))
codigo=int(input("Ingrese el codigo de su producto: "))
marca=str(input("Ingrese la marca del producto: "))
precio=float(input("Ingresa el precio del producto: "))
stock=int(input("Ingrese el stock del producto: "))
kiosko=[nombre,codigo,marca,precio,stock]
print(kiosko)
print()
kiosko1=[]
cod=2
while cod!=0:
    nombre=str(input("Ingrese el tipo del producto: "))
    codigo=int(input("Ingrese el codigo de su producto: "))
    marca=str(input("Ingrese la marca del producto: "))
    precio=float(input("Ingresa el precio del producto: "))
    stock=int(input("Ingrese el stock del producto: "))
    kiosko1.append(nombre,codigo,marca,precio,stock)	
    cod=int(input())
print (kiosko1)
