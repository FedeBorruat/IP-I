def pertenece2 (e,l:list) -> bool:
    res=False
    i=0
    while (i<(len(l))):
        if (e==l[i]):
            res=True
            i=i+(len(l))
        else:
            i=i+1
    return(res)
#print(pertenece2((6),[2,3,1]))

def pertenece (e:int, l:list[int]) -> bool:
    for i in range(len(l)):
        if e == l[i]:
            return(True)
        
def divide_a_todos (a:list[int], b:int) -> bool:
    global res
    while (len(a)!=0):
        if (( (a[0]) % b) != 0 ):
            a.pop(0)
            res=False
            divide_a_todos(a,b)
        else:
            a.pop(0)
            res=True
            divide_a_todos(a,b)
        return(res) 
#print(divide_a_todos(([6,8,64]),2))

def suma_total(s:list[int]) -> int:
    x=s.copy()
    while (len(x)!=1):
        x.insert(0,(x[0]+x[1]))
        x.pop(1)
        x.pop(1)
    return(x[0])
#print(suma_total([1,2,3,6]))

def ordenar(s:list[int]) -> bool:
    global res
    if (len(s)==1):
        res = True
    else:
        if ((s[0])<(s[1])):
            s.pop(0)
            ordenar(s)
        else:
            res=False
    return(res)    
#print(ordenar([1,2,3]))

def problema1_5 (s:list[str]) -> bool:
    global res
    if ((len(s))==1):
        res=True
    else:
        if (len(s[0]) < 7):
            res=False
        else:
            s.pop(0)
            problema1_5(s)
    return(res)
#print(problema1_5(["djfjhdjf","popopopo"]))

def palindromo(s:str) -> bool:
    global res
    f=(len(s)-1)
    i=0
    while(((f)>=i)and(s[i]==s[f])):
        i=i+1
        f=f-1
    if (s[i]!=s[f]):
        res=False
    else:
        res=True
    return(res)   
#print(palindromo("apppla"))

def fortaleza(contra:str) -> str:
    if (len(contra)<5):
        res="ROJO"
    else:
        if (len(contra)>8) and (tiene_min(contra)==True) and (tiene_may(contra)==True) and (tiene_num(contra)==True):
            res="VERDE"
        else:
            res="AMARILLO"
    return(res)

def tiene_min (s:str) -> bool:
    for i in range(len(s)):
        if ((s[i])>="a") and (s[i]<="z"):
            res=True
    return(res)
#print(tiene_min("f1Rjkjdfdf2342CCkjf"))

def tiene_may (s:str) -> bool:
    for i in range(len(s)):
        if ((s[i])>="A") and (s[i]<="Z"):
            res=True
    return(res)
#print(tiene_may("FFFf"))

def tiene_num (s:str) -> bool:
    for i in range(len(s)):
        if ((s[i])>="0") and (s[i]<="9"):
            res=True
    return(res)
#print(tiene_min("f1Rjkjdfdf2342CCkjf"))
#print(fortaleza("FFFFF333f"))

def mov_dinero (s:list[(chr,int)])-> int:
    saldo=0
    for i in range (len(s)):
        if ((s[i])[0]=="I"):
            saldo=saldo+(s[i])[1]
        else:
            saldo=saldo-(s[i])[1]
    return(saldo)
#print(mov_dinero([("I",500),("R",400)]))

def tres_vocales_dist (s:str) -> bool:
    a=[]
    for i in range(len(s)):
        if (((s[i])=="a")or(s[i]=="e")or(s[i]=="i")or(s[i]=="o")or(s[i]=="u"))and(not(s[i] in a)):
                a.append(s[i])
    if (len(a)>=3):
            res=True
    else:
            res=False
    return(res)
#print(tres_vocales_dist("aeiaaa"))

def cero_en_pares (s:list[int]) -> [int]:
    for i in range (len(s)):
        if (i%2==0):
            s[i]=0
    return(s)
#print(cero_en_pares([1,2,3,4]))

def cero_en_pares2 (s:list[int]) -> [int]:
    x=s
    for i in range (len(x)):
        if (i%2==0):
            s[i]=0
    return(x)
#print(cero_en_pares2([1,2,3,4]))

def sacar_vocales (s:[chr])->str:
    x=''
    for i in range (len(s)-1):
        if (not(s[i] in ["a","e","i","o","u","A","E","I","O","U"])):
            x=x+s[i]
    return(x)
#print(sacar_vocales ("hola"))

def remplazar_vocales (s:[chr]) -> [chr]:
    x=''
    for i in range(len(s)):
        if (s[i] in ["a","e","i","o","u"]):
            x = x + '_'
        else:
            x=x+s[i]
    return(x)
#print(remplazar_vocales("hola"))

def da_vuelta_str (s:[chr]) -> [chr]:
    alreves=''
    for i in range(len(s)):
        alreves = alreves + s[len(s)-1-i]
    return(alreves)
#print(da_vuelta_str('abcdeo'))

def eliminar_repetidos(s:[chr]) -> [chr]:
    x=''
    i=0
    while (i<len(s)):
        if pertenece2(s[i],x):
            i=i+1
        else:
            x=x+s[i]
            i=+1
            
    return(x)
#print(eliminar_repetidos("hoolaaaaad"))

def notas_mayor_a_4 (n:[int]) -> bool:
    i=0
    res=True
    while (i<(len(n))):
        if (n[i]>=4):
            i=i+1
        else:
            res=False
            i=i+(len(n))
    return(res)
#print(notas_mayor_a_4([4,3,6]))

def aprobado (n:[int]) -> int:
    x=(suma_total(n))
    prom=x//((len(n))-1)
    if (prom>=7) and (notas_mayor_a_4(n)):
        res=1
    elif (prom>=4) and (prom<7) and (notas_mayor_a_4(n)):
        res=2
    else:
        res=3
    return(res)
#print(aprobado([7,8,9,8,9,9]))

def lista_estudiantes () -> [str]:
    l=[]
    while (True):
        a=input()
        if (a == "listo"):
           return(l)
        else:
            l.append(a)
#print(lista_estudiantes())

def historial() -> [(str, int)]:
    historial=[]
    while (True):
        print(" C = Cargar creditos","\n","D = Descontar creditos","\n","X = Finalizar simulacion")
        operacion= input()
        if (operacion=="C"):
            print("Monto:")
            carga= input()
            historial.append((operacion, carga))
        elif (operacion=="D"):
            print("Monto:")
            carga= input()
            historial.append((operacion, carga))
        elif (operacion=="X"):
            return(historial)
        else:
            print("No se reconoce operacion")
#print(historial())

import random

def carta_random()->int:
    carta = random.randint(1,10)
    if (carta>7):
        return(0.5)
    else:
        return(carta)
#print(carta_random())

def siete_y_medio ()-> [int]:
    while True:
        carta=carta_random()
        sumahist=carta
        hist=[]
        while ((sumahist)<=(7.5)):
            print(" Su carta es:",carta,"Total:",sumahist,".","\n","Otra carta? (Si/No)")
            decision=input()
            if decision=="Si":
                hist.append(carta)
                carta=carta_random()
                sumahist=sumahist+carta
                hist.append(carta)
            elif decision=="No":
                return(hist)
        if ((sumahist)>(7.5)):
            print(sumahist)
            print("Perdiste!")
#print(siete_y_medio())

def pertenece_a_cada_uno_version_1 (s:[[int]], e:int, res:[bool]):
    res.clear()
    for i in range(len(s)):
        resu=pertenece2(e,s[i])
        res.append(resu)
        i=i+1
    print(res)
#pertenece_a_cada_uno_version_1([[1,2,3],[1,4,6],[3,4,5]],4,["hola"])   

def es_matriz (s:[[int]]) -> bool:
    res=True
    for i in range(len(s)):
        if len(s[0]) != len(s[i]):
            res=False
    return(res)
#print(es_matriz([[1,2],[2],[3,3]]))