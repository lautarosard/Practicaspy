list=[5,7,8,51,22,35,36,48,20,15,16,32]
print(list)
lista_pares=[]
lista_impares=[]
cant=0
cantneg=0
for n in list:
    if(n%2==0):
        lista_pares.append(n)
        cant=cant+1
    else:
        lista_impares.append(n)
        cantneg=cantneg+1
print("-"*50)
print("los numeros pares son: ", lista_pares)
print("la cantidad de numeros pares es: ",cant)
print("los numeros impares son: ", lista_impares)
print("la cantidad de numeros impares es: ",cantneg)
print("-"*50)