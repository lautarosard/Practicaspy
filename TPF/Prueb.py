from datetime import datetime
consulta=datetime.now().strftime('%d-%m-%Y')
print(consulta)
vencij=str(input('Ingrese fecha de vencimiento "aaaa/mm/dd: '))
fechaj= datetime.strptime(vencij, '%Y/%m/%d').strftime('%d-%m-%Y')
print (fechaj)
if consulta>fechaj:
    print(consulta,"ws mayor")