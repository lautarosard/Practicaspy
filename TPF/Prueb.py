from datetime import datetime
piojab=[]
consulta=datetime.now().strftime('%Y/%m/%d')
print(consulta)
vencij=str(input('Ingrese fecha de vencimiento "aaaa/mm/dd: '))
while vencij!="05/05/05":
    fechaj= datetime.strptime(vencij, '%Y/%m/%d').strftime('%Y/%m/%d')
    piojab.append(fechaj)
    print (piojab)
    for co in piojab:
        fechi=co[3]
        if fechi>consulta:
            piojab.append(co)
    vencij=str(input('Ingrese fecha de vencimiento "aaaa/mm/dd: '))
print(piojab,"ws mayor")
    

