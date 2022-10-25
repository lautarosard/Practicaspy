#personas for
print("lista de personas")
alumnos=[["Carlos",40],["Camila",19],["Tiziano",15],["Lucas",20]]
print(alumnos)
pernu=str(input("Agrega un alumno: "))
peredad=int(input("Cual es su edad: "))
alum=[pernu,peredad]
alumnos.append(alum)
cant=0
cantn=0
for alu in alumnos:
    if(alu[1]>=18):
        cant=cant+1
    else:
        cantn=cantn+1
print("-"*50)
print("La cantidad de alumnos Mayores es de: ",cant)
print("La cantidad de alumnos Menores es de: ",cantn)
print("-"*50)