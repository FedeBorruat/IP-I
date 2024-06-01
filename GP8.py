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
    while (archivo.readlines())!='':
        contenido=(archivo.readlines())
    print(contenido)

print(invertit_lineas('archivo.txt'))