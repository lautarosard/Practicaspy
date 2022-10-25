antiguedad=int(input("Ingrese su antiguedad en el trabajo: "))
sueldo=float(input("ingrese su sueldo: "))
porc=(sueldo)* 0.2
Banti=antiguedad*100
Sfinal=porc+sueldo+Banti
print("")
print("-"*110)
print("El porcentaje es de tu sueldo es de ",porc)
print("Por tus ", antiguedad," años de antiguedad tenes un aumento de ",
Banti)
print("Y tu sueldo final sera de", Sfinal) 
print("-"*110)
