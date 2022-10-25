ancho=float(input("Inserte el ancho del terreno; "))
largo=float(input("Inserte el largo del terreno; "))
sup=ancho*largo
#transf, pasa de m2 a cm2 y divide por el tamaño de los paneles (que es de 60*60)
transf=(sup*10000)/3600
#transf2 pasa de cm2 a m2
transf2=transf/10000
print("-"*50)
print("ancho: ",ancho," largo: ",largo)
print(sup,"M°2")
print("Se deberan colocar ",int( transf2)," paneles")
print("-"*50)
