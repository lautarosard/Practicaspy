#funciones
def calculo_rebaja(a,b):
    z=b*100/a
    return(z)
#program
d=float(input("Ingrese el precio original: "))
l=float(input("Ingrese el precio actual: "))
porce=calculo_rebaja(d,l)
print("El porcentaje de rebaja es del: ",porce," porciento")