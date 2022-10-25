#7 Calcular el área y perímetro de un círculo
import math
print("Calcular el área y perímetro de un circulo")
d=float(input("Ingrese el diametro del circulo: "))
area=d*math.pi
peri=(d/2)*math.pi**2
print("-"*55)
print("El área de su circulo es de: ",area,"\nEl perimetro de su circulo es de: ",peri)
print("-"*55)
