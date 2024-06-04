def contar_lineas (arc:str)->int:
    path=('/home/fede/Documentos/IP-I/Python/GP8/'+(arc))
    abrir_archivo=open(path,'r')
    contenido = abrir_archivo.readlines()
    abrir_archivo.close()
    return(len(contenido))
#print(contar_lineas('archivo.txt'))

def pertenece(e, l)->bool:
    res=False
    for i in range(len(l)):
        if e==l[i]:
            res=True
    return(res)    
#print(pertenece('\n','#comentario\n'))

def existe_palabra (palabra:str, arc:str) -> bool:
    res=False
    palabratexto=[]
    palabrachr=[]
    for i in palabra:
        palabrachr.append(i)
    path=('/home/fede/Documentos/IP-I/Python/GP8/'+arc)
    archivo= open(path,'r')
    for linea in archivo:   
        for caracter in linea:  
                if caracter==',' or caracter==' ':
                    if palabratexto==palabrachr:
                        res=True
                        palabratexto=[]
                    else:
                        palabratexto=[]
                else:
                    palabratexto.append(caracter)               
    archivo.close()
    
    return(res)
#print(existe_palabra('nombre','archivo.txt'))

def cantidad_de_apariciones (palabra:str, arc:str) -> bool:
    res=0
    palabratexto=[]
    palabrachr=[]
    for i in palabra:
        palabrachr.append(i)
    path=('/home/fede/Documentos/IP-I/Python/GP8/'+arc)
    archivo= open(path,'r')
    for linea in archivo:
        for palabras in linea:   
            for caracter in palabras:  
                if caracter==',' or caracter==' ':
                    if palabratexto==palabrachr:
                        res=res+1
                    else:
                        palabratexto=[]
                else:
                    palabratexto.append(caracter)               
    archivo.close()
    return(res)
#print(cantidad_de_apariciones('de','archivo.txt'))

def clonar_sin_comentarios (arc:str):
    path='/home/fede/Documentos/IP-I/Python/GP8/'
    viejo=(path+arc)
    nuevo=(path+'clonado.txt')
    archivo= open(viejo,'r+')
    clonado= open(nuevo,'w')
    linea=[]
    for lineas in archivo:
        for caracter in lineas:
            if caracter!='\n':
                if caracter=='#':
                    lineaSinEsp=linea.copy()
                    while pertenece(' ',lineaSinEsp)==True:
                        lineaSinEsp.remove(' ')
                    if((len(lineaSinEsp))==0): 
                        linea=[]
                        next(lineas)
                    else:
                        linea.append(caracter)
                else:
                    linea.append(caracter)
            else:
                linea.append(caracter)
                for i in range(len(linea)):
                    clonado.write(linea[i])
                linea=[]
    archivo.close()
    clonado.close()
    print('Listo!')
#print(clonar_sin_comentarios('archivo.txt'))

def invertit_lineas (arc: str): 
    path='/home/fede/Documentos/IP-I/Python/GP8/'
    viejo=(path+arc)
    nuevo=(path+'reverso.txt')
    archivo=open(viejo, 'r')
    inverso=open(nuevo, 'w')
    contenido=(archivo.readlines())
    x=len(contenido)
    primerlineainv:str
    if not(pertenece('\n',contenido[(len(contenido))-1])):
        primerlineainv = contenido[(len(contenido))-1] +'\n'
        inverso.write(primerlineainv)
        for i in range (len(contenido)):
            if i!=0:
                inverso.write(contenido[x-i-1])
    else:
        for i in range (len(contenido)):
            inverso.write(contenido[x-i-1])
        archivo.close
        inverso.close
#print(invertit_lineas('archivo.txt'))

def agregar_frase_al_final (arc: str, frase: str):
    path='/home/fede/Documentos/IP-I/Python/GP8/'
    archivoR=open(path+arc, 'r')
    contenido=(archivoR.readlines())
    archivoR.close()
    contenido.append('\n')
    contenido.append(frase)
    archivoW=open(path+'FraseAlFianl.txt', 'w')
    for i in range(len(contenido)):
        archivoW.write(contenido[i])
    archivoW.close()
#agregar_frase_al_final('archivo.txt','Hola')

def agregar_frase_al_principio (arc: str, frase: str):
    path='/home/fede/Documentos/IP-I/Python/GP8/'
    archivoR=open(path+arc, 'r')
    contenido=(archivoR.readlines())
    archivoR.close()
    archivoW=open(path+'FraseAlPrincipio.txt', 'w')
    archivoW.write(frase)
    archivoW.write('\n')
    for i in range(len(contenido)):
        archivoW.write(contenido[i])
    archivoW.close()
#gregar_frase_al_principio('archivo.txt', 'Holaaaa')

def hay_numeros (e) ->bool:
    res=False
    for i in range(len(e)):
        if e[i]>='0' and e[i]<='9':
            res=True
    return(res)
def hay_min (e) ->bool:
    res=False
    for i in range(len(e)):
        if e[i]>='a' and e[i]<='z':
            res=True
    return(res)
def hay_mayu (e) ->bool:
    res=False
    for i in range(len(e)):
        if e[i]>='A' and e[i]<='Z':
            res=True
    return(res)

def listar_palabras_de_archivos (arc: str) -> list:
    path='/home/Estudiante/Descargas/'
    archivo = open(path+arc,'br')
    cont= archivo.read()
    cont2=[]
    palle=[]
    for i in range(len(cont)):
        cont2.append(chr(cont[i]))
    for i in range(len(cont2)):
        if len(cont2[i])>=5 and (hay_numeros(cont2[i])) and ((hay_mayu(cont2[i]))or(hay_min(cont2[i]))) and (pertenece(' ',(cont2[i])) or pertenece('_',(cont2[i]))):
            palle.append(cont2[i])
    return(palle)
#print(listar_palabras_de_archivos('Archivo.zip'))

def calcular_promedio_estudiante (archivo_notas: str, archivo_promedios:str):
    path='/home/fede/Documentos/IP-I/Python/GP8/'
    notas=open(path+archivo_notas,'r')
    prom=open(path+'promedios.txt','w')
    contnotas=notas.readlines()
    contnotas2=''
    palabras=[]
    palabra=''
    palrever=''
    for i in range(len(contnotas)):
        contnotas2=contnotas2+contnotas[i]
    for i in range(len(contnotas2)):
        if contnotas2[i]!='_' and contnotas2[i]!='\n' :
            palabra=contnotas2[i]+palabra
        else:
            for i in range(len(palabra)):
                palrever= palabra[i]+palrever
            palabras.append(palrever)
            palabra=''
            palrever=''
    for i in range (len(palabras)):
        palabra=palabra+'!'+palabras[i]
    palabra=palabra+'!'
    prom.write(palabra)
#calcular_promedio_estudiante('notas.txt','')    
    
def promedio_estudiante(arc:str, nlu:str)-> float:
    path='/home/fede/Documentos/IP-I/Python/GP8/'
    archivo=open(path+arc, 'r')
    cont=archivo.readlines()
    contarc=''
    palabras=[]
    nota=[]
    lu=[]
    palabra=''
    palrever=''

    for i in range(len(cont)):
        contarc=contarc+cont[i]

    for i in range(len(contarc)):
        if contarc[i]!='!':
            palabra=contarc[i]+palabra
        else:
            for i in range(len(palabra)):
                palrever= palabra[i]+palrever
            palabras.append(palrever)
            palabra=''
            palrever=''

    for i in range(len(palabras)): 
        if len(palabras[i])==1 or len(palabras[i])==2 :
            nota.append(palabras[i])
            lu.append(palabras[i-3])
    prom=0
    n=0
    for i in range(len(lu)):
        if nlu==lu[i]:
            prom=prom+int((nota[i]))
            n=n+1

    prom=prom/n
    return(prom)
#print(promedio_estudiante('promedios.txt','155'))

from queue import LifoQueue
import random

def generar_nros_al_azar_pila(cantidad:int, desde:int, hasta:int) -> [int]:
    pila = LifoQueue()
    while (pila.qsize()!=cantidad):
        n=random.randint(desde,hasta)
        pila.put(n)
    return(pila)
#print(generar_nros_al_azar(2,0,10).queue)

def cantidad_de_elemetnos (p:[int]) -> int:
    x=p.copy()
    l=LifoQueue()
    for i in range(len(x)):
        l.put(x[i])
    i=0
    while not(l.empty()):
        i=i+1
        l.get()
    return i
#print(cantidad_de_elemetnos([1]))

def buscar_el_maximo (p:LifoQueue[int]) -> int:
    for r in range(p.qsize()-1):
        x=l.get()
        y=l.get()
        if x<y:
            l.put(y)
        else:
            l.put(x)
    h=l.get()
    return(h)
#print(buscar_el_maximo(l))

def evaluar_expresion(s:str) -> float:
    op=LifoQueue()
    el=LifoQueue()
    for i in range(len(s)):
        x=(len(s)-i)-1
        if s[x]=='+':
            op.put(s[x])
        elif s[x]=='-':
            op.put(s[x])
        elif s[x]=='*':
            op.put(s[x])
        elif s[x]=='/':
            op.put(s[x])
        elif (s[x]>='0' and s[x]<='9'):
            el.put(s[x])
    while not(op.empty()):
        a=op.get()
        if a=='+':
            A= el.get()
            B= el.get()
            C=int(A)+int(B)
            el.put(C)
        elif a=='-':
            A= el.get()
            B= el.get()
            C=int(A)-int(B)
            el.put(C)
        elif a=='*':
            A= el.get()
            B= el.get()
            C=int(A)*int(B)
            el.put(C)
        elif a=='/':
            A= el.get()
            B= el.get()
            C=int(A)/int(B)
            el.put(C)
    D=el.get()
    return(D)
#print(evaluar_expresion("3 4 + 5 * 2 -"))

from queue import Queue

def generar_nros_al_azar_cola():
    cola=Queue()
    x=random.randint(0,100)
    cola.put(x)
#(generar_nros_al_azar_cola())

def cant_elementos(c:Queue)-> int:
    i=0
    while not(c.empty()):
        c.get()
        i=i+1
    return(i) 
#print(cant_elementos(a))

def armar_secuancia_de_bingo() -> Queue[int]:
    c=Queue()
    n=[]
    while len(n)!=100:
        x=random.randint(0,99)
        if not(pertenece(x,n)):
            n.append(x)
    for i in range(len(n)):
        c.put(n[i])
    return(c)
#print(armar_secuancia_de_bingo().queue)

def jugar_carton_de_bingo(carton:list[int],bolillero:Queue[int])->int:
    carton1=carton.copy()
    bolillero1=Queue()
    G=bolillero.get()
    bolillero1.put(G)
    bolillero.put(G)
    while (bolillero.qsize() != bolillero1.qsize()):
        a=bolillero.get()
        bolillero1.put(a)
        bolillero.put(a)    
    i=0
    tiradas=0
    while i!=12:
        b=bolillero1.get()
        tiradas=tiradas+1
        if pertenece(b,carton1):
            i=i+1
    print(bolillero.queue)
    return(tiradas)
C=Queue()
C.put(1)
C.put(2)
C.put(3)
C.put(4)
C.put(5)
C.put(6)
C.put(7)
C.put(8)
C.put(9)
C.put(10)
C.put(11)
C.put(12)

#print(jugar_carton_de_bingo([1,2,3,4,5,6,36,8,9,10,11,12],armar_secuancia_de_bingo()))

def n_pacientes_urgentes (c:Queue[(int,str,str)]) -> int:
    c1=Queue()
    a=c.get()
    c1.put(a)
    c.put(a)    
    while c.qsize() != c1.qsize():
        A=c.get()
        c1.put(A)
        c.put(A)
    prioridad=Queue()
    while not(c1.empty()):
        b=c1.get()
        if int(b[0])>=0 and int(b[0])<=3:
            prioridad.put(b)
    return(prioridad.qsize())
hospital=Queue()
hospital.put((2,'j','j'))
hospital.put((1,'j','j'))
hospital.put((8,'j','j'))
hospital.put((6,'j','j'))
hospital.put((8,'j','j'))
#print(n_pacientes_urgentes(hospital))

def Banco (ficha: Queue[(str,int,bool,bool)]) -> Queue[(str,int,bool,bool)]:
    ficha1=Queue()
    a=ficha.get()
    ficha1.put(a)
    ficha.put(a)
    while ficha1.qsize() != ficha.qsize():
        A=ficha.get()
        ficha1.put(A)
        ficha.put(A)
    prioridad=Queue()
    preferencial=Queue()
    resto=Queue()
    while not(ficha1.empty()):
        b=ficha1.get()
        if b[3]==True:
            prioridad.put(b)
        elif b[2]==True and b[3]==False:
            preferencial.put(b)
        else:
            resto.put(b)
    orden=Queue()
    while not(prioridad.empty()):
        c=prioridad.get()
        orden.put(c)
    while not(preferencial.empty()):
        d=preferencial.get()
        orden.put(d)
    while not(resto.empty()):
        r=resto.get()
        orden.put(r)
    return(orden)
Lista=Queue()
Lista.put(('AA',23423423,True,False))
Lista.put(('AB',23423345,True,False))
Lista.put(('AC',23424445,True,True))
Lista.put(('AD',23455566,True,True))
Lista.put(('AE',23423454,False,True))
Lista.put(('AF',23423567,True,False))
Lista.put(('AG',23423456,False,False))
Lista.put(('AH',23423420,False,False))
#print(Banco(Lista))

