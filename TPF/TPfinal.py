#librer
from datetime import datetime
#Farmacia de Florencio Varela
#Funciones
def medblister(lis):
    blist=[]
    for vin in lis:
        if vin[2]=="blister":
            blist.append(vin)
    return blist

def jarnostock(lis):
    jar=[]
    for van in lis:
        if van[5]<=0:
            jar.append(van)
    return jar

def actstock(lis):
    cont=1
    print('De cual laboratorio desea actualizar el stock:')
    for lib in lis:
        print(lib[3])
    labi=input('Laboratorio: ')
    for led in lis:
        if labi==led[3]:
            led[6]=int(input('Ingrese el nuevo stock: '))
    print(lis)
    
def caducidad(list,cad):
    piojab=[]
    for co in list:
        if co[3]>cad:
            piojab.append(co)
    return piojab

#Programa
print('*'*55)
print("Bienvenido a la farmacia")
print('*'*25)
print('rellene los datos de el/los medicamento/s y del/los jarabe/s')
print('*'*55)
#PASTI
med_pastillas=[]
codpas=str(input("Código del medicamento: "))
while codpas!="AAA":
    nompas=str(input('Nombre del medicamento: '))
    prese=str(input('Blister/botella: '))
    labp=str(input('Laboratorio: '))
    vencip=str(input('Ingrese fecha de vencimiento "aaaa/mm/dd: '))
    fechav= datetime.strptime(vencip, '%Y/%m/%d').strftime('%d-%m-%Y')
    pventa=float(input('Precio de venta: '))
    stockp=int(input('Stock del medicamento: '))
    listpasti=[codpas,nompas,prese,labp,fechav,pventa,stockp]
    med_pastillas.append(listpasti)
    print('*'*55)
    print('Para parar la carga de datos ingrese "AAA"')
    codpas=str(input("Código del medicamento: "))
#Codeína
med_jarabe=[]
print('*'*55)
codjara=str(input("Código del jarabe: "))
while codjara!="zzz":
    nomjar=str(input('Nombre del jarabe: '))
    labj=str(input('Laboratorio: '))
    vencij=str(input('Ingrese fecha de vencimiento "aaaa/mm/dd: '))
    fechaj= datetime.strptime(vencij, '%Y/%m/%d').strftime('%d-%m-%Y')
    jventa=float(input('Precio de venta: '))
    stockj=int(input('Stock del medicamento: '))
    lisjarab=[codjara,nomjar,labj,fechaj,jventa,stockj]
    med_jarabe.append(lisjarab)
    print('Para parar la carga de datos ingrese "zzz"')
    codjara=str(input("Código del jarabe: "))
print('*'*55)
print('pastillas',med_pastillas)
print('*'*55)
print('jarabes',med_jarabe)
print('*'*55)
#pacio
consulta=datetime.now().strftime('%d-%m-%Y')
#princi
menu='''
1.Medicamentos en Blister
2.Jarabes cuyo stock es de 0
3.Actualizar el stock del medicamento de una farmacia
4.jarabes cuya fecha de vencimiento es mayor al dia que se hace la consulta
5.Salir
'''
print(menu)
opc=str(input('Ingrese la opción que quiere: '))
while opc!="5":
    if opc=="1":
        blist=medblister(med_pastillas)
        print(blist)
        print(menu)
        opc=str(input('Ingrese la opción que quiere: '))
    elif opc=="2":
        zstock=jarnostock(med_jarabe)
        print(zstock)
        print(menu)
        opc=str(input('Ingrese la opción que quiere: '))
    elif opc=="3":
        actstock(med_pastillas)
        print(menu)
        opc=str(input('Ingrese la opción que quiere: '))
    elif opc=="4":
        aptojab=caducidad(med_jarabe, consulta)
        print(aptojab)
        print(menu)
        opc=str(input('Ingrese la opción que quiere: '))
print('Salio del programa.')