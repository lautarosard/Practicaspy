#funci
def porce(r,d):
    x=(r*d)/100
    return x

#Programa principal
print('Calcular el porcentaje. \nSi quiere salir del programa ingrese el numero 0')
num1=0
num2=0
limit=1
while limit!=0:
	num1=int(input('Ingrese el numero que representa el porcentaje: '))
	num2=int(input('Ingrese el numero que representa el número entero: '))	
	print("El porcentaje que representa es: ",porce(num1,num2))
	limit=int(input('Si quiere salir del programa ingrese 0, sino, cualquier otro: '))
