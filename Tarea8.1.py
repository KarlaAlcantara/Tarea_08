#encoding: UTF-8
#Karla Valeria Alcantara Duarte
#Tarea 8 listas


def sumarAcumulacion(a):
    x = []
    acumulador = 1
    for k in range(len(a)):
        valor = a[k]
        x.append(acumulador)
        acumulador += valor + 1
    return x

def quitarPrimUl(a):
    x = list(a)
    for valor in range (len(x)):
        x.pop(0)
        x.pop()
        return x

def ordenLista(a):
    b = list(a)
    lista = sorted(b)
    if a==lista:
        return True
    else:
        return False

def buscarAnagrama(a,b):
    a1 = sorted(a)
    b1 = sorted(b)
    if a1==b1:
        return True
    else:
        return False


def examinarLista(a):
    for k in a:
        if a.count(k)>=2:
            return True

    return False



def  eliminarRepetidos(a):
    for valor in range(len(a)):
        num = a.count(valor)
        if num >= 2:
            a.pop(valor)

    return a


def main():

    a = [1,2,3,4,5,6]
    b = [1,1,2,2,3,3]
    c = [7,9,9,8,0]
    d = [1,2,3]
    g = ["A","B","C","B","D","E","X","F"]
    j = ["1","2","3","4"]
    cadena1 = "TomMarvoloRiddle"
    cadena2 = "IamLordVoldemort"
    h = list(cadena1.lower())
    i = list(cadena2.lower())

    funcion1 = sumarAcumulacion(d)
    print(d)
    print(funcion1)
    print("----------------------------------------------")
    funcion2 = quitarPrimUl(a)
    print(a)
    print(funcion2)
    print("----------------------------------------------")
    print(g)
    funcion3 = ordenLista(g)
    print (funcion3)
    print(j)
    funcion3 = ordenLista(j)
    print(funcion3)
    print("----------------------------------------------")
    print(cadena1, cadena2)
    funcion4 = buscarAnagrama(h, i)
    print(funcion4)
    print("----------------------------------------------")
    funcion5 = examinarLista(c)
    print(c)
    print(funcion5)
    print("----------------------------------------------")
    print(b)
    funcion6 = eliminarRepetidos(b)
    print(funcion6)
    print("----------------------------------------------")

main()