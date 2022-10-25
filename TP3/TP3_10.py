def calculo_transporte(a,v,c,d):
    s=(a+v+c)+3*3
    return(int(s/d))
#Programa
c1=int(input("sala 1: "))
c2=int(input("sala 2: "))
c3=int(input("sala 3: "))
m=int(input("asientos: "))
print("Se necesitan ",calculo_transporte(c1,c2,c3,m)," Micros")