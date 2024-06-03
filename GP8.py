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
#agregar_frase_al_principio('archivo.txt', 'Holaaaa')

def listar_palabras_de_archivos (arc: str) -> list:
    path='/home/fede/Documentos/IP-I/Python/GP8/'
    archivo = open(path+arc,'br')
    cont= archivo.read()
    chr(byte)
    print(cont)
    return([])

listar_palabras_de_archivos('archivo.txt')