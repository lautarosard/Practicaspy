#6 tablas de mult
def tablas(a):
    tabs=[(1,("1x1",1,"2x2",2))]
    h=tabs[a-1]
    return(h)
num=int(input("Cual es el tabla desea: "))
print(tablas(num))
