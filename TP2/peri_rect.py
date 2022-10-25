#Funci
def peri_rect(a,b):
	x=a*2+b*2
	return(x)
#Programa
print('Calculación del perimetro de un rectangulo')
largo=float(input('Ingrese el largo de su rectangulo: '))
ancho=float(input('Ingrese el ancho de su rectangulo: '))
peri=peri_rect(largo,ancho)
print('El perimetro de su rectangulo es de: ',peri)