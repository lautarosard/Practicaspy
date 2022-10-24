#Funci
def cargarDatos():
    nom=str(input('Ingrese su nombre: '))
    ape=str(input('Ingrese su apellido: '))
    edad=int(input('Ingrese su edad: '))
    suel=float(input('Ingrese su sueldo: '))
    ld=[nom,ape,edad,suel]
    return (ld)
def esMayorDeEdad(pers):
    if pers[2]<=18:
        return True
    else:
        return False
def personaMejorSueldo(pers1,pers2):
    if pers1[3]>pers2[3]:
        return pers1
    else:
        return pers2
def personaMasJoven(pers1,pers2):
    if pers1[2]<pers2[2]:
        return pers1
    else:
        return pers2
#Program
print('Bienvenidos/as al programa sobre datos de personas')
print('Se va a solicitar los datos de 2 personas y va a mostrar información sobre ellas')
pers=[]
pers1=cargarDatos()
pers2=cargarDatos()
pers.append(pers1)
pers.append(pers2)
print(pers)
print('La persona que gana más es: ', personaMejorSueldo(pers1,pers2))
print('La más chica es: ', personaMasJoven(pers1,pers2))
#if personaMejorSueldo(pers1,pers2)
