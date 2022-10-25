#fuciones
def convertir_a_dolar(a):
    x=a/146
    return(x)
def convertir_a_euro(a):
    x=a/142
    return(x)
def convertir_a_real(a):
    x=a/27.5
    return(x)
#Program
p=float(input("ingrese la cantidad de pesos que desea convertir: "))
dolar=convertir_a_dolar(p)
euro=convertir_a_euro(p)
real=convertir_a_real(p)
print("-"*100)
print("La conversión a dolar es: ",dolar,"\nEn Euro es de: ",euro,"\nEn Real es de: ",real)
