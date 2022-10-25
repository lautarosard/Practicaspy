#funci
def peri(a,b,c):
	x=float(a+b+c)
	return(x)

def area(a,b):
	z=float((a*b)/2)
	return(z)
#Programa
print("Area y perimetro de un triangulo")
base=float(input("ingrese la base de su triangulo: "))
altura=float(input("ingrese la altura de su triangulo: "))
lado1=float(input("ingrese la medida del lado: "))
lado2=float(input("ingrese la medida del otro lado: "))
p=peri(base,lado1,lado2)
a=area(base,altura)
print("-"*20)
print("El area de su triangulo es de: ",a,"\nEl perimetro de su triangulo es de: ",p)
