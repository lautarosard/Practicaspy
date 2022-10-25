nom=input("Ingrese su nombre: ")
apell=input("Ingrese su apellido: ")
fecha=str(input("Ingrese la fecha de nacimiento en este formato *dd/mm/aaaa*: "))
print(nom, apell, fecha)
print(nom[0]+apell[0]+"_"+fecha[:2]+fecha[3:5]+fecha[6:])
print(nom[-1].lower())
	
