#Funciones
def calculo_litros(a,c,d):
    m=(a*c*d)*1000
    return str(m)+"L"
#Programa
nu1=float(input("Ingrese el alto: "))
nu2=float(input("Ingrese el ancho: "))
nu3=float(input("Ingrese la profundidad: "))
print("La cantidad de litros que \npuede contener la pileta es de: ", calculo_litros(nu1,nu2,nu3))