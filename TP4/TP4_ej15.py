from Funciones import *

#Funciones
def funcidofun(a):
    if a==1:
        num1=float(input("Ponga el precio base: "))
        num2=float(input("En porcentaje, cuanto le desea aumentar: "))
        print(calculo_nuevo_precio(num1,num2))
    elif a==2:
        c1=int(input("sala 1: "))
        c2=int(input("sala 2: "))
        c3=int(input("sala 3: "))
        m=int(input("asientos: "))
        print("Se necesitan ",calculo_transporte(c1,c2,c3,m)," Micros")
    elif a==3:
        nu1=float(input("Ingrese el alto: "))
        nu2=float(input("Ingrese el ancho: "))
        nu3=float(input("Ingrese la profundidad: "))
        print("La cantidad de litros que \npuede contener la pileta es de: ", calculo_litros(nu1,nu2,nu3))
    elif a==4:
        ds=int(input("Ingrese la cantidad de días que va a medicarse: "))
        ct=int(input("Ingrese la cantidad que tiene que tomar por día: "))
        pasti=int(input("Ingrese cantidad de pastillas que tiene el envase:"))
        if calculo_dosis(ds,ct,pasti)==True:
            print("El envase va a alcanzar para el tratamiento")
        else:
            print("La cantidad de pastillas no le van a alcanzar \npara su tratamiento")
    else:
        print("Opción no disponible")
#programa principal
print("Hola bienvenido/a a este programa, seleccione una de las opciones")
print("1-Calcular precio","\n2-Calcular transporte","\n3-Calcular litros","\n4-Calcular dosis",)
