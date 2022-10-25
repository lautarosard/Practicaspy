def calculo_nuevo_precio(a,b):
     porc=(b/100)*a+a
     return(porc)
def calculo_transporte(a,v,c,d):
    s=(a+v+c)+3*3
    return(int(s/d))
def calculo_litros(a,c,d):
    m=(a*c*d)*1000
    return str(m)+"L"
def calculo_dosis(a,v,d):
    p=a*v
    if p>d:
        return(False)
    else:
        return(True)
