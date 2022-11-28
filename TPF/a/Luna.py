import openpyxl
book= openpyxl.load_workbook("BOLETIN.xlsx", data_only=True)
hoja=book.active
celda = hoja["A2":"F7"]
notas= []
for fila in celda:
    nota=[celda.value for celda in fila]
    notas.append(nota)

def boletin(notas,nom):
    for sa in notas:
        if sa[0]==nom:
            
def matematicas(notas,nom):
    mate=0
    for vi in notas:
        if nom==vi[0]:
            mate=vi[1]
    return mate
def lengua(notas):
    a=1
    if (nombre==notas[a:0]):
        leng=notas [a:2]
    else:
        a=a+1
    return leng
def sociales(notas):
    a=1
    if (nombre==notas[a:0]):
        soc=notas [a:3]
    else:
        a=a+1
    return soc
def biologia(notas):
    a=1
    if (nombre==notas[a:0]):
        bio=notas [a:4]
    else:
        a=a+1
    return bio
def promedio(notas):
    a=1
    if (nombre==notas[a:0]):
        pro=notas [a:5]
    else:
        a=a+1
    return pro
print(notas)
nombre=str(input("Ingrese el nombre del estudiante(En mayuscula): "))
menu='''
1)Nota de Matematica
2)Nota de Lengua
3)Nota de Sociales
4)Nota de biologia
5)Promedio total
6)Boletin
7)Salir
'''
print(menu)
opcion=int(input("Elija una opcion: "))
while opcion!=7:
    if (opcion==1):
        mate=matematicas(notas,nombre)
        print(mate)
        print(menu)
        opcion=int(input("Elija una opcion: "))
    elif (opcion==2):
        leng=lengua(notas)
        print(leng)
        print(menu)
        opcion=int(input("Elija una opcion: "))
    elif (opcion==3):
        soc=sociales(notas)
        print(soc)
        print(menu)
        opcion=int(input("Elija una opcion: "))
    elif (opcion==4):
        bio=biologia(notas)
        print(bio)
        print(menu)
        opcion=int(input("Elija una opcion: "))
    elif (opcion==5):
        prom=promedio(notas)
        print(prom)
        print(menu)
        opcion=int(input("Elija una opcion: "))
    elif(opcion==6):
        boletin(notas,nombre)
        print(menu)
        opcion=int(input("Elija una opcion: "))
        
print("Salio del programa")
