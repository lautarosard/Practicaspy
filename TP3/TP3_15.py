#Funciones
def calculo_dosis(a,v,d):
    p=a*v
    if p>d:
        return(False)
    else:
        return(True)
#programa
ds=int(input("Ingrese la cantidad de días que va a medicarse: "))
ct=int(input("Ingrese la cantidad que tiene que tomar por día: "))
pasti=int(input("Ingrese cantidad de pastillas que tiene el envase:"))
if calculo_dosis(ds,ct,pasti)==True:
    print("El envase va a alcanzar para el tratamiento")
else:
    print("La cantidad de pastillas no le van a alcanzar \npara su tratamiento")