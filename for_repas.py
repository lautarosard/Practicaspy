kiosko=[[110,"chocolatada","Nesquik",250,3],[100, "alfajor", "jorgito", 200, 15], [103, "chocolate", "Aguila", 350, 0],
[101, "cocacola", "cocacola", 250, 3], [104, "chocolinas", "chocolinas", 400, 0], [106, "galletas", "fantoche", 300, 6],
[107, "galletas", "soda", 200, 0], [101, "alfajor", "jorgito", 400, 15]]
print (kiosko)
print ()
for elem in kiosko:
    print (elem)
#lista de productos de 0
print("-"*10)
nostock=[]
print("Los productos sin stock son:")
for vin in kiosko:
    if vin[4]==0:
        print('-'*5)
        print(vin[0],"||",vin[2])
        nostock.append(vin)
print('-'*5)
print(nostock)
#lista del más caro
print("-"*10)
cod=0
max=0
name=""
for ell in kiosko:
    if ell[3]>max:
        cod=ell[0]
        name=ell[2]
        max=ell[3]
print("El producto más caro es: ",name,cod,"$"+str(max),)
print("-"*10)
#Más barato
print("-"*10)
cod1=0
min=34149848
name1=""
for la in kiosko:
    if  la[3]<min    :
        cod1=la[0]
        name1=la[2]
        min=la[3]
print("El producto más barato es: ",name1,cod1,"$"+str(min),)
print("-"*10)
        

