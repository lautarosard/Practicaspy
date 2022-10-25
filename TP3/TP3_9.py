#Funciones
def calculo_nuevo_precio(a,b):
     porc=(b/100)*a+a
     return(porc)
#Programa
num1=float(input())
num2=float(input())
print(calculo_nuevo_precio(num1,num2))
