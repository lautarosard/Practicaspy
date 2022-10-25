#Funciones
def CargarFraccion():
    num=int(input("Ingrese el numerador de la fracción: "))
    den=int(input("Ingrese el denominador de la fracción: "))
    frac=[num,den]
    return(frac)

def numfrac(u):
    return (u[0])
def denfrac(u):
    return (u[1])

def multifrac(w,e):
    num=w[0]*e[0]
    den=w[1]*e[1]
    return ([num,den])

def divfrac(w,e):
    num=w[0]*e[1]
    den=w[1]*e[0]
    return ([num,den])

def sumafrac(w,e):
    if(w[1]==e[1]):
        num=w[0]+e[0]
        return (num,w[1])
    else:
        eqden=w[1]*e[1]
        num1=w[0]*e[1]
        num2=w[1]*e[0]
        return([(num1+num2),eqden])

def restfrac(w,e):
    if(w[1]==e[1]):
        num=w[0]-e[0]
        return (num,w[1])
    else:
        eqden=w[1]*e[1]
        num1=w[0]*e[1]
        num2=w[1]*e[0]
        return([(num1-num2),eqden])
#Programa principal
print("Operaciones con fracciones")
frac1=CargarFraccion()
frac2=CargarFraccion()
print("-"*50)
print ("El denominador de la primera fraccion es: ", frac2[1])
print ("El numerador de la segunda fraccion es: ", frac2[0])
print ("La suma de dichas fracciones es: ",sumafrac(frac1,frac2))
print ("La resta de dichas fracciones es: ",restfrac(frac1,frac2))
print ("La multiplicación de dichas fracciones es: ",multifrac(frac1,frac2))
print ("La division es: ", divfrac(frac1,frac2))
print("-"*50)
