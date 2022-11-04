from tkinter import *
from tkinter import messagebox
import re
"""Palabras claves
Homepage-> Ventana principal de saludo
Mainpage-> Ventana de ingreso de polinomios(Inicio de la calculadora)
Bloqueuno-> Pantalla donde hay un solo bloque para escribir
Bloquedos-> Pantalla donde hay dos bloques para escribir
"""
def verificacaracter(string): #Podria ser mas especifico
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

def listtostring(polinomio):
    stringlist=[]
    for i in range(len(polinomio)):
        if polinomio[i][1] != 0 and polinomio[i][1] != 'NULL':
            temp=str(polinomio[i][0])+'x^'+str(polinomio[i][1])
            stringlist.append(temp)
        elif polinomio[i][1] == 0 and polinomio[i][0] !=0:
            temp=str(polinomio[i][0])
            stringlist.append(temp)

    #for i in range(len(stringlist)): stringlist.pop(i) if stringlist[i] == '' else 0 #Cuando derivam

    temp='+'.join(stringlist)
    temp=temp.replace('+-','-')

    return temp


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

#Casos 
firstclick=True #-> Sirve para controlar el cursor

#Opciones
def raicespol(polinomioingresado):
    polinomiostring=polinomioingresado[0]
    valorx=polinomioingresado[1]
    valory=polinomioingresado[2]
    
    print("CASO 1",polinomioingresado[0],polinomioingresado[1],polinomioingresado[2])
    return polinomioingresado

def maxminpol(polinomioingresado):
    polinomiostring=polinomioingresado[0]
    valorx=polinomioingresado[1]
    valory=polinomioingresado[2]

    print("CASO 2",polinomioingresado[0],polinomioingresado[1],polinomioingresado[2])
    return polinomioingresado

def derivapol(polinomioingresado):
    derivadastring=polinomioingresado[0]
    print("CASO 3",polinomioingresado[0])
    #Primero separamos el polinomio en una matriz de acuerdo a la cantidad de terminos
    polinomio=separapolinomio(derivadastring)
    print(f"Antes de derivar {derivadastring}")
    for i in range(len(polinomio)):
        if polinomio[i][1] == 0:
            polinomio[i][0]=0
        elif polinomio[i][1]=='NULL':
            polinomio[i][0]=0
        else:
            #Bajamos el exponente y multiplicamos al coeficiente
            polinomio[i][0]*=polinomio[i][1]
            #Restamos uno al exponente
            polinomio[i][1]-=1
    
    
    #Pasamos la matriz a formato polinomio
    polformat=listtostring(polinomio)
    print(f"Despues de derivar {polformat}")


    return polformat

def integrapol(polinomioingresado):
    print("CASO 4",polinomioingresado[0],polinomioingresado[1],polinomioingresado[2])
    return polinomioingresado

def graficapol(polinomioingresado,ventana): #2x^3+6 -> 2x**3+6
    gra=Toplevel(ventana)
    gra.grab_set()
    print("CASO 5",polinomioingresado[0],polinomioingresado[1],polinomioingresado[2])
    return polinomioingresado

def sumpol(polinomioingresado):
    print("Caso 1 doble",polinomioingresado[0],polinomioingresado[1])
    return polinomioingresado

def mulpol(polinomioingresado):
    print("Caso 2 doble",polinomioingresado[0],polinomioingresado[1])
    return polinomioingresado

#Funcion centrar
#Sirve para centrar cada ventana nueva abierta al centro del monitor donde se abre la aplicacion
def centrar(root):
    root.resizable(False,False)
    appwidth = 1000
    appheight= 650
    screenwidth = root.winfo_screenwidth() 
    screenheight = root.winfo_screenheight() 
    x =(screenwidth/2) - (appwidth/2) 
    y =(screenheight/2) - (appheight/2) 
    root.geometry(f"{appwidth}x{appheight}+{int(x)}+{int(y)}")


"""Dados dos casos en los cuales se deban de usar mismos botones(+,-,x,etc) para cuadros de textos distintos, posi = 1-> indica que el boton se introduzca en el cuadro de texto
                                                                                                              posi = 2-> indica que el boton se introduzca al siguiente cuadro de texto"""
posi=1   

#Ultima pagina
def ultima(bloquetipo,verifica,ingresolista):
    def leavethird2add():#Dejamos la ultima fase para volver a la ventana donde se ingresan mas polinomios
        resultado.destroy()
        secondpage()
    def leavethird2home():#Dejamos la ultima fase para volver a la ventana donde empieza todo
        resultado.destroy()
        main()
    def leavethird2opt():#Sujeto a cambios-> Pero en si, si funcionase el boton nos llevaria al menu de opciones con el o los mismos polinomios elegidos inicialmente para proceder a trabajar sobre ellos nuevamente
        resultado.destroy()
        opcionmenu(bloquetipo,polinomioingresado=ingresolista[0],polinomioingresado2=ingresolista[1])  #Agregar bien el bloquetipo

    #Debido a que las listas son opciones del menu de acuerdo a la variable que se provea de verifica ahi se va a empezar a comparar para saber que operacion hacer, por consiguiente
    #En caso de casos especiales, eventualmente se agregaran mas parametros en la funcion de forma de poder identificar de manera eficiente que operacion realizar

    opciones1 = ['Obtener raíces reales de la ecuación ', 'Obtener puntos máximos y mínimos de la función ', 'Calcular la derivada de la función ', 'Calcular la integral de la función','Graficar el polinomio']
    opciones2 = ['Obtener suma de polinomios', 'Obtener producto de dos polinomios']
    resultado=Tk()
    centrar(resultado)

    #En cada caso se deberia de llamar a la funcion de cada caso y como parametros deberia de tener el polinomio mandado 
    respuesta='' 
    if verifica in opciones1:

        casodado=opciones1.index(verifica)
        if casodado == 0:
            respuesta=raicespol(ingresolista) 
        elif casodado == 1:
            respuesta=maxminpol(ingresolista) 
        elif casodado == 2:
            respuesta=derivapol(ingresolista) 
        elif casodado == 3:
            respuesta=integrapol(ingresolista) 
        elif casodado == 4:
            respuesta=graficapol(ingresolista,resultado) 

    elif verifica in opciones2:
        casodado1=opciones2.index(verifica)
        if casodado1 == 0:
            respuesta=sumpol(ingresolista)
        elif casodado1 == 1:
            respuesta=mulpol(ingresolista)


    #Abrimos nuestra ultima ventana


    #Fondo ultima fase
    bg1 = PhotoImage(file="ico/Last page.png")
    bg2 = PhotoImage(file="ico/Last page 2.png")
    label1 = Label(resultado,image=bg1)
    label1.place(x=0,y=0,relwidth=1,relheight=1)

    #Sujeto a cambios de orden
    #Respuesta
    if verifica != 'Graficar el polinomio': 
        answer=Label(resultado,text=respuesta,font=('Arial',11),bg='white',width=60,height=2).place(x=223,y=334)


    #Botones
    #Realizar mas operaciones
    ejecutatarea = PhotoImage(file="ico/nuevaop.png")
    ejecutalabel = Label(image=ejecutatarea)
    ejecutaboton = Button(resultado,image=ejecutatarea,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=leavethird2opt,cursor="hand2")
    ejecutaboton.place(x=818,y=335)

    #Agregar mas polinomios
    ingresamas = PhotoImage(file="ico/ingresamas.png")
    ingresalabel = Label(image=ingresamas)
    ingresamasboton = Button(resultado,image=ingresamas,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=leavethird2add,cursor="hand2")
    ingresamasboton.place(x=33,y=609)

    #Volver al homepage 
    irahomepage = PhotoImage(file="ico/Salir.png")
    iralabel = Label(image=irahomepage)
    irahomeboton = Button(resultado,image=irahomepage,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=leavethird2home,cursor="hand2")
    irahomeboton.place(x=722,y=607)


    resultado.mainloop()

#Menu de opciones
def opcionmenu(bloquetipo,**datosingresados):#Ya que el numero de elementos por caso varia usamos el parametro **kwargs
    polinomioingresado=datosingresados.get('polinomioingresado') #Obtenemos la entrada 1
    polinomioingresado2=datosingresados.get('polinomioingresado2')#Obtenemos la entrada 2

    def gobackinput():#Del menu de opciones volver a la pagina donde se ingresan los polinomios
        options.destroy()
        secondpage()

    def clickopt(): #Una vez elegida la opcion el boton de continuar nos redirige aca


        def gotothirdspecial(especifica,polinomioingresado):  #gotothirdspecial sirve para redireccionar los datos de x e y para ciertas funciones especiales que lo necesitaron
            punto1=varx.get()
            punto2=varx2.get()
            bloque1=[polinomioingresado,punto1,punto2]
            varxey.destroy()
            ultima(bloquetipo,especifica,bloque1) #La especifica seria la operacion a realizar, ya sea suma,mult,raices,etc
        
        def gobackinput():#En caso de querer volver al input
            varxey.destroy()
            secondpage()
            
        #De acuerdo al proceso elegido pasamos una variable ESPECIFICA a la tercera pagina (podria ser-> tener que introducir dos variables mas o directo a la pagina de resultados)
        options.destroy()
        opcionesespeciales=['Obtener raíces reales de la ecuación ', 'Obtener puntos máximos y mínimos de la función ', 'Calcular la integral de la función','Graficar el polinomio']
        especifica = opcelegida1.get()


        if especifica not in opcionesespeciales:
            if bloquetipo == 1:
                bloque1=[polinomioingresado,polinomioingresado2]
                ultima(bloquetipo,especifica,bloque1)
            else:
                bloque2=[polinomioingresado,polinomioingresado2]
                ultima(bloquetipo,especifica,bloque2)

        elif especifica in opcionesespeciales: #Los casos especiales son cuando se deba de ingresar dos variables, x1 y x2 para trabajar con ellas
            def validapuntos():
                if not entradanx1.get() and entradanx2.get():
                    messagebox.showinfo("Alerta","La celda 1 no puede estar vacia")
                elif not entradanx2.get() and  entradanx1.get() :
                    messagebox.showinfo("Alerta","La celda 2 no puede estar vacia")
                elif not entradanx2.get() and  not entradanx1.get() :
                    messagebox.showinfo("Alerta","La celdas no pueden estar vacias")
                else:
                    gotothirdspecial(especifica,polinomioingresado)

            varxey=Tk()
            centrar(varxey)
            bg1 = PhotoImage(file="ico/casoespecial.png")
            label1 = Label(varxey,image=bg1)
            label1.place(x=0,y=0,relwidth=1,relheight=1)
            
            #Text boxes
            varx=StringVar()
            varx2=StringVar()
            
            entradanx1=Entry(varxey,textvariable=varx,width=50,border=0,font=('Arial',12),cursor="xterm")
            entradanx1.place(x=450, y=309, width=120, height=20)

            entradanx2=Entry(varxey,textvariable=varx2,width=50,border=0,font=('Arial',12),cursor="xterm")
            entradanx2.place(x=450, y=375, width=120, height=20)


            #Botones
            ejecutatarea = PhotoImage(file="ico/Siguientee.png")
            ejecutalabel = Label(image=ejecutatarea)
            ejecutaboton = Button(varxey,image=ejecutatarea,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=validapuntos,cursor="hand2")
            ejecutaboton.place(x=635,y=333)

            atrasimg = PhotoImage(file="ico/back.png")
            atraslabel = Label(image=atrasimg)
            atrasboton = Button(varxey,image=atrasimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=gobackinput,cursor="hand2")
            atrasboton.place(x=4,y=553)

            varxey.mainloop()

    #Desplegar las opciones disponibles de acuerdo al bloquetipo
    def elegir(opciones):
        opcelegida1.set(opciones[0]) #Aca debe de variar

        #Menu desplegable 1
        drop = OptionMenu(options,opcelegida1,*opciones) #Aca debe variar

        #Hasta aca en una funcion
        drop.config(width=60,bg='white',activebackground='white',highlightthickness=0,bd=0,font=('Arial',12),fg='gray',cursor="hand2")
        drop.place(x=199,y=349)
    def validaopcion():
        if opcelegida1.get() != opciones1[0]:
            clickopt()
        else:
            messagebox.showinfo("Alerta","Seleccione una opción")

    options=Tk()
    centrar(options)
    #Declaraciones de opciones disponibles
    opciones1 = ['                                                                               Seleccione una opción                                                                      ','Obtener raíces reales de la ecuación ', 'Obtener puntos máximos y mínimos de la función ', 'Calcular la derivada de la función ', 'Calcular la integral de la función','Graficar el polinomio']
    opciones2 = ['                                                                               Seleccione una opción                                                                      ','Obtener suma de polinomios', 'Obtener producto de dos polinomios']
    opcelegida1 = StringVar()

    bg1 = PhotoImage(file="ico/Menu desplega.png")
    label1 = Label(options,image=bg1)
    label1.place(x=0,y=0,relwidth=1,relheight=1)
    #Condicionales para saber las opciones disponibles
    if bloquetipo == 1:
        elegir(opciones1)
    elif bloquetipo == 2:
        elegir(opciones2)

    ejecutatarea = PhotoImage(file="ico/Siguiente.png")
    ejecutalabel = Label(image=ejecutatarea)
    ejecutaboton = Button(options,image=ejecutatarea,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',cursor="hand2",command=validaopcion).place(x=825,y=347)

    #Boton de retroceder de opciones a ingreso de polinomios
    atrasimg = PhotoImage(file="ico/back.png")
    atraslabel = Label(image=atrasimg)
    atrasboton = Button(options,image=atrasimg,borderwidth=0,bg="#B9CED9",command=gobackinput,activebackground='#B9CED9',cursor="hand2")
    atrasboton.place(x=4,y=553)

    options.mainloop()

def secondpage():
    def goback():
        mainpage.destroy()
        main()
    def main1tomain2():
    #Esta Funcion cambia del frame con un solo bloque para escribir a otra con dos bloques
        bloquedos.pack(fill='both', expand=1)
        bloqueuno.forget()

    def main2tomain1():
    #Esta Funcion cambia del frame con dos bloques para escribir a otra con un bloque
        bloqueuno.pack(fill='both', expand=1)
        bloquedos.forget()
    def botonclick(caracter,posi):
        posicion=entradanombre0.index(INSERT)
        posicion2=entradanombre1.index(INSERT)
        if posi == 1:
            entradanombre0.insert(posicion,caracter)

        elif posi == 2:
            entradanombre1.insert(posicion2,caracter) 

    def cambio(click):
        global posi
        posi= click
        
    def main2opt(bloquetipo,polinomioingresado,polinomioingresado2):
        mainpage.destroy()
        opcionmenu(bloquetipo,polinomioingresado=polinomioingresado,polinomioingresado2=polinomioingresado2)

    def validarentrada(bloquetipo):
        polinomio0ingresado=stringvar0.get()
        polinomio1ingresado=stringvar1.get()
        

        if bloquetipo == 1:
            if not entradanombre0.get():
                messagebox.showinfo("Alerta","La celda no puede estar vacia")

            #Agregar else dp
            else:
                if verificacaracter(polinomio0ingresado):
                    check1=separapolinomio(polinomio0ingresado)
                    if verificaexponente(check1):
                        main2opt(bloquetipo,polinomio0ingresado,polinomio1ingresado)
                    else:
                        messagebox.showinfo("Alerta","Verifique que todos los exponentes esten dentro del rango 0<exp<=12")
                else:
                    messagebox.showinfo("Alerta","Por Favor utilice los botones prestablecido para introducir el polinomio")
        else:

            if not entradanombre0.get() and entradanombre1.get() :
                messagebox.showinfo("Alerta","La celda 1 no puede estar vacia")
            elif not entradanombre1.get() and entradanombre0.get():
                messagebox.showinfo("Alerta","La celda 2 no puede estar vacia")
            elif not entradanombre1.get() and not entradanombre0.get():
                messagebox.showinfo("Alerta","La celdas no pueden estar vacias")

            #Agregar else dp
            else:
                if verificacaracter(polinomio0ingresado) and verificacaracter(polinomio1ingresado):
                    check1=separapolinomio(polinomio0ingresado)
                    check2=separapolinomio(polinomio1ingresado)
                    if verificaexponente(check1) and verificaexponente(check2):
                        main2opt(bloquetipo,polinomio0ingresado,polinomio1ingresado)
                    else:
                        messagebox.showinfo("Alerta","Verifique que todos los exponentes esten dentro del rango 0<exp<=12")
                        
                else:
                    messagebox.showinfo("Alerta","Por favor utilice los botones prestablecido para introducir el polinomio")
                    messagebox.showinfo("Alerta","No esta permitido el uso de letras")

                #main2opt(bloquetipo,polinomio0ingresado,polinomio1ingresado)

    mainpage = Tk()
    mainpage.title("Calculadora de polinomios")
    centrar(mainpage)

    #Creamos los dos frames para el Mainpage-> Se iran cambiando en caso de requirimiento
    bloqueuno=Frame(mainpage)
    bloquedos=Frame(mainpage)

    #Mainpage 1
    #Fondo para Bloque uno
    bg1 = PhotoImage(file="ico/Ingrese 1.png")
    label1 = Label(bloqueuno,image=bg1)
    label1.place(x=0,y=0,relwidth=1,relheight=1)
    
    stringvar0=StringVar()
    entradanombre0=Entry(mainpage,textvariable=stringvar0,width=76,border=0,font=('Arial',12),cursor="xterm")
    entradanombre0.place(x=212.1, y=340, width=613, height=20)
    def gotovalid(event):
        validarentrada(1)

    entradanombre0.bind('<Return>',gotovalid) #ver si dejar o no
    #Botones 
    #Botones de operaciones aritmeticas
    #Suma
    sumaimg = PhotoImage(file="ico/Suma.png")
    sumalabel = Label(image=sumaimg)
    sumaboton1 = Button(bloqueuno,image=sumaimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('+',1),cursor="hand2")
    sumaboton1.place(x=448,y=374)

    #Resta
    restaimh = PhotoImage(file="ico/Resta.png")
    restalabel = Label(image=restaimh)
    restaboton = Button(bloqueuno,image=restaimh,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('-',1),cursor="hand2")
    restaboton.place(x=483,y=374)

    #Exponente
    expimg = PhotoImage(file="ico/Exponente.png")
    explabel = Label(image=expimg)
    expboton1 = Button(bloqueuno,image=expimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('^',posi),cursor="hand2")
    expboton1.place(x=518,y=374)

    #Boton para añadir un bloque de texto mas (nos lleva al frame 2)
    desplegaimg = PhotoImage(file="ico/Anadir.png")
    desplegalabel = Label(image=desplegaimg)
    desplegaboton = Button(bloqueuno,image=desplegaimg,borderwidth=0,command=main1tomain2,bg="#B9CED9",activebackground='#B9CED9',cursor="hand2")
    desplegaboton.place(x=169,y=333)

    #Boton de ir a la siguiente ventana-> IR A MENU DE OPCIONES
    proceder1 = PhotoImage(file="ico/Siguiente.png")
    procedelabel1 = Label(image=proceder1)
    procedeboton1 = Button(bloqueuno,image=proceder1,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:validarentrada(1),cursor="hand2")
    procedeboton1.place(x=843,y=332)

    #Retroceder a la Homepage
    atrasimg = PhotoImage(file="ico/back.png")
    atraslabel = Label(image=atrasimg)
    atrasboton = Button(bloqueuno,image=atrasimg,borderwidth=0,command=goback,bg="#B9CED9",activebackground='#B9CED9',cursor="hand2")
    atrasboton.place(x=4,y=553)

    #Mainpage 2
    bg2 = PhotoImage(file="ico/Ingrese 2.png")
    label2 = Label(bloquedos,image=bg2)
    label2.place(x=0,y=0,relwidth=1,relheight=1)

    #Bloque de texto
    stringvar1=StringVar()
    entradanombre1=Entry(bloquedos,textvariable=stringvar1,width=76,border=0,font=('Arial',12),cursor="xterm")
    entradanombre1.place(x=212.1, y=382, width=613, height=20)
    def gotovalid2(event):
        validarentrada(2)

    entradanombre1.bind('<Return>',gotovalid2) #ver si dejar o no


    #Sirve para cuando toquemos un bloque los botones sirvan ahi, caso contrario para el siguiente bloque y asi
    entradanombre0.bind("<FocusIn>",lambda e:cambio(1))
    entradanombre0.bind("<FocusOut>",lambda e:cambio(2))  

    entradanombre1.bind("<FocusIn>",lambda e:cambio(2))
    entradanombre1.bind("<FocusOut>",lambda e:cambio(1))  
    
    #Botones
    #Botones de operaciones aritmeticas
    #Suma
    sumaboton = Button(bloquedos,image=sumaimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('+',posi),cursor="hand2")
    sumaboton.place(x=448,y=415)

    #Resta
    restaboton1 = Button(bloquedos,image=restaimh,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('-',posi),cursor="hand2")
    restaboton1.place(x=483,y=415)

    #Exponente
    expboton1 = Button(bloquedos,image=expimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('^',posi),cursor="hand2")
    expboton1.place(x=518,y=415)

    #Boton de ir al menu de opciones-> Solo nos permite dos opciones(Debido a que con dos polinomios solo se puede hacer suma o resta)
    proceder = PhotoImage(file="ico/Siguiente.png")
    procedelabel = Label(image=proceder)
    procedeboton = Button(bloquedos,image=proceder,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:validarentrada(2),cursor="hand2")
    procedeboton.place(x=845,y=357)


    #Boton para volver al bloque donde hay un solo bloque de texto (Lo escrito en el primer bloque no se borra para ahorra tiempo de carga de polinomio)
    desplegaimg1 = PhotoImage(file="ico/minimice.png")
    desplegalabel1 = Label(image=desplegaimg1)
    desplegaboton1 = Button(bloquedos,image=desplegaimg1,borderwidth=0,command=main2tomain1,bg="#B9CED9",activebackground='#B9CED9',cursor="hand2")
    desplegaboton1.place(x=166,y=333)

    
    #Volver a la homepage
    atrasimg1 = PhotoImage(file="ico/back.png")
    atraslabel1 = Label(image=atrasimg1)
    atrasboton1 = Button(bloquedos,image=atrasimg1,borderwidth=0,command=goback,bg="#B9CED9",activebackground='#B9CED9',cursor="hand2")
    atrasboton1.place(x=4,y=553)

    bloqueuno.pack(fill='both', expand=1)
    mainpage.mainloop()



def main():
    #Sirve para empezar todo el proceso en si e ir a la nueva ventana 
    def nextpageboton():
        homepage.destroy()
        secondpage()
    
    #Declaramos nueva ventana
    homepage = Tk()
    homepage.title("Calculadora de polinomios")
    centrar(homepage)

    #Fondo del homepage
    bg = PhotoImage(file="ico/Homepage.png")
    label = Label(homepage,image=bg)
    label.place(x=0,y=0,relwidth=1,relheight=1)

    #Boton para dirigirnos a la siguiente ventana
    starimg = PhotoImage(file="ico/Empiece.png")
    starlabel = Label(image=starimg)
    starbutton = Button(homepage,image=starimg,borderwidth=0,command=nextpageboton,cursor="hand2")
    starbutton.place(x=335,y=416)

    homepage.mainloop()

main()