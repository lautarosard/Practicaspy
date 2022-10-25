#Definicion de funciones
def sumaAlcuadrado(x, y):
    rta= x**2 + 2*x*y + y**2
    return (rta)
#Programa principal
print ("Bienvenidos/as a la Suma al Cuadrado")
a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
print (sumaAlcuadrado(a, b))
