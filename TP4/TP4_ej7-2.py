#Funci
def cargp():
    nom=str(input())
    ape=str(input())
    sueld=float(input())
    cat=str(input())
    antig=int(input())
    perso=[nom,ape,sueld,cat.upper(),antig]
    return perso

#program
#perso=cargp()
nom=str(input("Ingrese su nombre: "))
ape=str(input("Ingrese su apellido: "))
sueld=float(input("Ingrese su sueldo: "))
cat=str(input("Ingrese su en que categoría esta A/B/C: "))
antig=int(input("Ingrese su antiguedad: "))
perso=[nom,ape,sueld,cat.upper(),antig]
print(perso)

if cat=="A":
    if perso[4]<10:
        sueldfin=perso[2]+(perso[2]*5)/100
        print("Su sueldo con una antiguedad de 10 años o menos: ",sueldfin)
    elif perso[4]>=10 and perso[4]<=15:
        sueldfin=perso[2]+(perso[2]*10)/100
        print("Su sueldo con una antiguedad entre 10 y 15 años es de: ",sueldfin)   
    elif perso[4]>15:
        sueldfin=perso[2]+(perso[2]*15)/100
        print("Su sueldo con una antiguedad de 15 años o más es de: ",sueldfin)

if perso[3]=="B":
    if perso[4]<10:
        sueldfin=perso[2]+(perso[2]*10)/100
        print("Su sueldo con una antiguedad de 10 años o menos: ",sueldfin)
    elif perso[4]>=10 and perso[4]<=15:
        sueldfin=perso[2]+(perso[2]*15)/100
        print("Su sueldo con una antiguedad entre 10 y 15 años es de: ",sueldfin)
    elif perso[4]>15:
        sueldfin=perso[2]+(perso[2]*20)/100
        print("Su sueldo con una antiguedad de 15 años o más es de: ",sueldfin)

if perso[3]=="C":
    if perso[4]<10:
        sueldfin=perso[2]+(perso[2]*15)/100
        print("Su sueldo con una antiguedad de 10 años o menos: ",sueldfin)
    elif perso[4]>=10 and perso[4]<=15:
        sueldfin=perso[2]+(perso[2]*20)/100
        print("Su sueldo con una antiguedad entre 10 y 15 años es de: ",sueldfin)
    elif perso[4]>15:
        sueldfin=perso[2]+(perso[2]*25)/100
        print("Su sueldo con una antiguedad de 15 años o más es de: ",sueldfin)     

