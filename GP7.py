def pertenece2 (e:int, l:list[int]) -> bool:
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
    while (len(s)!=1):
        s.insert(0,(s[0]+s[1]))
        s.pop(1)
        s.pop(1)
    return(s[0])

#print(suma_total([1,2,3,6]))

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
