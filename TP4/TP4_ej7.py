#Funciones
def talles(l,c):
    if l in range(15,19) and c in range(18,19):
        x=1
        return(x)
    elif l in range(19,23) and c in range(20,22):
        x=2
        return(x)
    elif l in range(25,28) and c in range(22,24):
        x=3
        return(x)
    elif l in range(28,31) and c in range(24,26):
        x=4
        return(x)
    elif l in range(31,37) and c in range(26,30):
        x=5
        return(x)
    elif l in range(37,46) and c in range(30,36):
        x=6
        return(x)
    elif l in range(46,56) and c in range(36,41):
        x=7
        return(x)
    else:
        x=8
        return(x)
    
   
#Programa principal
l=int(input("Ingrese el largo(cm); "))
c=int(input("Ingrese el contorno del cuello(cm); "))
print('-'*50)
print("Es el talle: ", talles(l,c))
print('-'*50)
