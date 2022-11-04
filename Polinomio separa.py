import re
def verificacaracter(string): #Podria ser mas especifico se puede arreglar mas
    habilitado=['0','1','2','3','4','5','6','7','8','9','^','-','+','x']

    num=0
    exp=0

    controla=0
    for i in string:
        if i in habilitado[:10]:
            num+=1
        elif i in habilitado[10:]:
            exp+=1
        
    if num+exp == len(string) and num !=0:
        return True
    elif num+exp != len(string):
        return False
    return False

def verificaexponente(matriz):
    #Vemos si todos los exponentes son > 0 y <=12
    cont=0
    cont1=0
    for i in range(len(matriz)):
        if not isinstance(matriz[i][1],str):
            if matriz[i][1] > 0 and matriz[i][1] <= 12:
                cont+=1
        else:
            cont1+=1
    if cont+cont1 == len(matriz):
        return True
    return False


def separapolinomio(string):
    #Ya que es mucho mas facil separar el string con split hacemos lo siguiente
    
    #En caso de que haya espacios vacios, los eliminamos
    string =string.replace(' ','')
    #Ya que es mas facil separar cada termino separado por el signo +
    #Procedemos a hacer lo siguiente
    string = re.sub('\^-', 'neg', string) #Primero-> En caso de encontrar exponentes negativos - > cambiarlo por el identificador neg
    string=string.replace('-','+-')       #Segundo-> A cada negativo que encontremos le agregamos un + al principio ya que a la hora de separar, lo hara de manera mas eficiente
    string=string.replace('neg','^-')     #Tercero-> Reemplazamos el identificador neg por lo que le corresponde que seria -> ^-


    sub = string.split('+')               #Separamos cada termino en una lista

    if sub[0]=='':
        temp=sub.index('')
        sub.pop(temp)

    print(sub)
    #Creamos nuestra matriz que tendra el siguiente formato-> (Por la cantidad de terminos introducidos se crearan Nx2 boxes, donde -> [coeficiente, exponente])
    matrizpol=[]
    for i in range(len(sub)):
        matrizpol.append([0,0])
    #Empezamos a guardar los coeficientes y exponentes
    for i in range(len(sub)):
        #Tenemos dos casos, terminos con o sin exponentes
        if '^' in sub[i]: #En caso de exponentes vemos donde comienza
            expindice=sub[i].index('^')
            
            if sub[i][0] != 'x' and sub[i][0:2] !='-x': 
                print('es',sub[i][0])
                matrizpol[i][0]=int(sub[i][0:expindice-1])
                
            elif sub[i][0] == 'x':
                matrizpol[i][0]=1 

            elif sub[i][0:2] == '-x' :
                matrizpol[i][0]=-1

            matrizpol[i][1]=int(sub[i][expindice+1:])
            
        elif '^' not in sub[i] and 'x' not in sub[i]:
            matrizpol[i][0]=int(sub[i])
            matrizpol[i][1]='NULL'
        elif '^' not in sub[i] and 'x' in sub[i]:
            xindice=sub[i].index('x')
            matrizpol[i][0]=int(sub[i][:xindice])
            matrizpol[i][1]=1
    
    return matrizpol


s='355 +     122x^5 +-325x^5 -122x^-4' 
s='-20x-3x^12+2x^1+3x+55'
temp = separapolinomio(s)
T=verificaexponente(temp)
print(temp,T)