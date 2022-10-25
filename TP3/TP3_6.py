#5 meses
def cuantos_dias(a):
    meslist=[("Enero",31),("Febrero",28),("Marzo",31),("Abril",30),("Mayo",31),("Junio",30),("Julio",31),("Agosto",31),("Septiembre",30),("Octubre",31),("Noviembre",30),("Diciembre",31)]
    z=meslist[a]
    return(z)

num=int(input("Ingresa el mes que quiere: "))
print(cuantos_dias(num))