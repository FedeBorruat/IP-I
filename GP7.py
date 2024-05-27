def pertence (a:list[int], b:int) -> bool:
    res=False
    while(len(a)!=0):
        if (a[0]==b):
            res=True
        else:
            a.pop(0)
            pertence(a,b)
    return(res)

#print(pertence([1,2,3],7))

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

def ordenar(s:list[int]) -> bool:
  