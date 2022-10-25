edad=int(input("ingrese su edad: "))
if edad>=0 and edad<=2:
    print("Bebe")
elif edad>2 and edad<=13:
    print("Niño/a")
elif edad>13 and edad<=20:
    print("Adolescente")
else:
    print("Adulto")