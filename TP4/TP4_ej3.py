#Funciones
def es_Divisible(n,m):
    x=m%n 
    if (x==0):
        return(True)
    else:
        return(False)
    
#Programa principal
print("Bienvenidos\as, este programa te va a decir si tus \nnúmeros son divisibles entre sí.")
n1=int(input("Ingrese un número: "))
n2=int(input("Ingrese un número por el que quiera dividir: "))
print('-'*50)
if (es_Divisible(n2,n1)==True):
    print("Su número es divisible ya que su resto es cero")
else:
    print("Su número no es divisible ya que su resto es diferente de cero")
print('-'*50)