from tkinter import *

"""Palabras claves
Homepage-> Ventana principal de saludo
Mainpage-> Ventana de ingreso de polinomios(Inicio de la calculadora)
Bloqueuno-> Pantalla donde hay un solo bloque para escribir
Bloquedos-> Pantalla donde hay dos bloques para escribir
"""

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
                                                                                                              posi = 2-> indica que el boton se introduzca al siguiente cuadro de texto
"""
posi=1         


#A partir de secondpage ya se incluye las siguientes caracteristicas
'''Posibilidad de escribir los polinomios
   Ir al menu de opciones-> Donde las opciones disponibles varian de acuerdo a la cantidad de polinomios ingresados'''

def secondpage():

    #Esta funcion nos permite ir a la ultima fase de nuestra interfaz donde se realizaran los procesos de acuerdo a la opcion elegida, y se mostrara en pantalla

    def thirdpage(verifica):
        def leavethird2add():#Dejamos la ultima fase para volver a la ventana donde se ingresan mas polinomios
            resultado.destroy()
            secondpage()
        def leavethird2home():#Dejamos la ultima fase para volver a la ventana donde empieza todo
            resultado.destroy()
            main()
        def leavethird2opt():#Sujeto a cambios-> Pero en si, si funcionase el boton nos llevaria al menu de opciones con el o los mismos polinomios elegidos inicialmente para proceder a trabajar sobre ellos nuevamente
            resultado.destroy()
            gonext() 

        #Debido a que las listas son opciones del menu de acuerdo a la variable que se provea de verifica ahi se va a empezar a comparar para saber que operacion hacer, por consiguiente
        #En caso de casos especiales, eventualmente se agregaran mas parametros en la funcion de forma de poder identificar de manera eficiente que operacion realizar

        opciones1 = ['Obtener raíces reales de la ecuación ', 'Obtener puntos máximos y mínimos de la función ', 'Calcular la derivada de la función ', 'Calcular la integral de la función','Graficar el polinomio']
        opciones2 = ['Obtener suma de polinomios ', 'Obtener producto de dos polinomios']

        #Abrimos nuestra ultima ventana
        resultado=Tk()
        centrar(resultado)


        #Espacio para comparacianos, llamadas a funciones etc

        #Espacio para comparacianos, llamadas a funciones etc


        #Fondo ultima fase
        bg1 = PhotoImage(file="ico/Last page.png")
        label1 = Label(resultado,image=bg1)
        label1.place(x=0,y=0,relwidth=1,relheight=1)


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
        irahomeboton.place(x=783,y=609)


        resultado.mainloop()

    def goback():#Volvemos al menu principal de saludo
        mainpage.destroy()
        main()



    def gonext(bloquetipo):#Nos dirijimos al menu de opciones para los o el polinomio elegido
        def gobackmain1():#En caso de querer retroceder del menu de opciones al menu de ingreso de polinomios hacemos lo siguiente
            options.destroy()
            secondpage()

        #Declaramos la nueva ventana y la colocacion de los widgets correspondientes
        mainpage.destroy()
        options=Tk()
        centrar(options)

        #Fondo
        bg1 = PhotoImage(file="ico/Menu desplega.png")
        label1 = Label(options,image=bg1)
        label1.place(x=0,y=0,relwidth=1,relheight=1)

        #Funcion para empezar el proceso de calculo especifico de acuerdo a lo elegido por el usuario
        #La variable especifica indica la opcion elegida, eventualmente se anadiran mas opciones de forma de hacer mas eficiente el proceso de ejecucion de calculos
        def clickopt1():
            def gotothirdspecial(especifica):
                varxey.destroy()
                thirdpage(especifica) #LE MANDAMOS ESPECIFICA PARA SABER QUE OPERACION REALIZAR
            
            def gobackinput():
                varxey.destroy()
                secondpage()
                
            #De acuerdo al proceso elegido pasamos una variable ESPECIFICA a la tercera pagina (podria ser-> tener que introducir dos variables mas o directo a la pagina de resultados)
            options.destroy()


            opcionesespeciales=['Obtener raíces reales de la ecuación ', 'Obtener puntos máximos y mínimos de la función ', 'Calcular la integral de la función','Graficar el polinomio']
            especifica = opcelegida1.get()

            if especifica not in opcionesespeciales:
                thirdpage(especifica)

            elif especifica in opcionesespeciales: #Los casos especiales son cuando se deba de ingresar dos variables, x1 y x2 para trabajar con ellas
                varxey=Tk()
                centrar(varxey)
                bg1 = PhotoImage(file="ico/casoespecial.png")
                label1 = Label(varxey,image=bg1)
                label1.place(x=0,y=0,relwidth=1,relheight=1)

                #Text boxes
                entradanx1=Entry(varxey,width=50,border=0,font=('Arial',12),cursor="xterm")
                entradanx1.place(x=450, y=309, width=120, height=20)

                entradanx2=Entry(varxey,width=50,border=0,font=('Arial',12),cursor="xterm")
                entradanx2.place(x=450, y=375, width=120, height=20)

                #Botones
                ejecutatarea = PhotoImage(file="ico/Siguientee.png")
                ejecutalabel = Label(image=ejecutatarea)
                ejecutaboton = Button(varxey,image=ejecutatarea,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:gotothirdspecial(especifica),cursor="hand2")
                ejecutaboton.place(x=635,y=333)

                atrasimg = PhotoImage(file="ico/back.png")
                atraslabel = Label(image=atrasimg)
                atrasboton = Button(varxey,image=atrasimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=gobackinput,cursor="hand2")
                atrasboton.place(x=4,y=553)

                varxey.mainloop()

        #Declaraciones de opciones disponibles
        opciones1 = ['                                                                               Seleccione una opción                                                                      ','Obtener raíces reales de la ecuación ', 'Obtener puntos máximos y mínimos de la función ', 'Calcular la derivada de la función ', 'Calcular la integral de la función','Graficar el polinomio']
        opciones2 = ['                                                                               Seleccione una opción                                                                      ','Obtener suma de polinomios ', 'Obtener producto de dos polinomios']
        opcelegida1 = StringVar()

        #Desplegar las opciones disponibles de acuerdo al bloquetipo
        def elegir(opciones):
            opcelegida1.set(opciones[0]) #Aca debe de variar

            #Menu desplegable 1
            drop = OptionMenu(options,opcelegida1,*opciones) #Aca debe variar

            #Hasta aca en una funcion
            drop.config(width=60,bg='white',activebackground='white',highlightthickness=0,bd=0,font=('Arial',12),fg='gray',cursor="hand2")
            drop.place(x=199,y=349)

        #Condicionales para saber las opciones disponibles
        if bloquetipo == 1:
            elegir(opciones1)
        elif bloquetipo == 2:
            elegir(opciones2)

        ejecutatarea = PhotoImage(file="ico/Siguiente.png")
        ejecutalabel = Label(image=ejecutatarea)
        ejecutaboton = Button(options,image=ejecutatarea,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=clickopt1,cursor="hand2").place(x=825,y=347)
        #Boton de retroceder de opciones a ingreso de polinomios
        atrasimg = PhotoImage(file="ico/back.png")
        atraslabel = Label(image=atrasimg)
        atrasboton = Button(options,image=atrasimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=gobackmain1,cursor="hand2")
        atrasboton.place(x=4,y=553)

        options.mainloop()

    
    def main1tomain2():
    #Esta Funcion cambia del frame con un solo bloque para escribir a otra con dos bloques
        bloquedos.pack(fill='both', expand=1)
        bloqueuno.forget()

    def main2tomain1():
    #Esta Funcion cambia del frame con dos bloques para escribir a otra con un bloque
        bloqueuno.pack(fill='both', expand=1)
        bloquedos.forget()


    #Creamos la ventana de inicio
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

    #Entrada de texto Bloque uno que sirve para Bloque dos de igual manera
    entradanombre0=Entry(mainpage,width=76,border=0,font=('Arial',12),cursor="xterm")
    entradanombre0.place(x=212.1, y=340, width=613, height=20)


    #Botones 
    #Botones de operaciones aritmeticas
    #Suma
    sumaimg = PhotoImage(file="ico/Suma.png")
    sumalabel = Label(image=sumaimg)
    sumaboton1 = Button(bloqueuno,image=sumaimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('+',1),cursor="hand2")
    sumaboton1.place(x=367,y=372)

    #Resta
    restaimh = PhotoImage(file="ico/Resta.png")
    restalabel = Label(image=restaimh)
    restaboton = Button(bloqueuno,image=restaimh,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('-',1),cursor="hand2")
    restaboton.place(x=402,y=372)

    #Multiplicar
    multimg = PhotoImage(file="ico/Multiply.png")
    mulabel = Label(image=multimg)
    multboton1 = Button(bloqueuno,image=multimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('x',posi),cursor="hand2")
    multboton1.place(x=437,y=372)

    #Division
    divimg = PhotoImage(file="ico/Dividir.png")
    dilabel = Label(image=divimg)
    divisionboton1 = Button(bloqueuno,image=divimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('/',posi),cursor="hand2")
    divisionboton1.place(x=475,y=372)

    #Exponente
    expimg = PhotoImage(file="ico/Exponente.png")
    explabel = Label(image=expimg)
    expboton1 = Button(bloqueuno,image=expimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('^',posi),cursor="hand2")
    expboton1.place(x=513,y=372)

    #Raiz
    raizimg = PhotoImage(file="ico/Raiz.png")
    ralabel = Label(image=raizimg)
    raizboton1 = Button(bloqueuno,image=raizimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('√',posi),cursor="hand2")
    raizboton1.place(x=551,y=371)

    #Parentesis abierto
    paroimg = PhotoImage(file="ico/Parentesis abierto.png")
    parlabel = Label(image=paroimg)
    paropenboton1 = Button(bloqueuno,image=paroimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('(',posi),cursor="hand2")
    paropenboton1.place(x=589,y=372)

    #Parentesis cerrado
    parcimg = PhotoImage(file="ico/Parentesis cerrado.png")
    parclabel = Label(image=parcimg)
    parcloseboton1 = Button(bloqueuno,image=parcimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick(')',posi),cursor="hand2")
    parcloseboton1.place(x=627,y=372)


    #Boton de ir a la siguiente ventana-> IR A MENU DE OPCIONES
    proceder1 = PhotoImage(file="ico/Siguiente.png")
    procedelabel1 = Label(image=proceder1)
    procedeboton1 = Button(bloqueuno,image=proceder1,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:gonext(1),cursor="hand2")
    procedeboton1.place(x=843,y=332)

    #Boton para añadir un bloque de texto mas (nos lleva al frame 2)
    desplegaimg = PhotoImage(file="ico/Anadir.png")
    desplegalabel = Label(image=desplegaimg)
    desplegaboton = Button(bloqueuno,image=desplegaimg,borderwidth=0,command=main1tomain2,bg="#B9CED9",activebackground='#B9CED9',cursor="hand2")
    desplegaboton.place(x=169,y=333)

    #Retroceder a la Homepage
    atrasimg = PhotoImage(file="ico/back.png")
    atraslabel = Label(image=atrasimg)
    atrasboton = Button(bloqueuno,image=atrasimg,borderwidth=0,command=goback,bg="#B9CED9",activebackground='#B9CED9',cursor="hand2")
    atrasboton.place(x=4,y=553)

    #Mainpage 2 configuracion
    #Fondo para Bloque dos
    bg2 = PhotoImage(file="ico/Ingrese 2.png")
    label2 = Label(bloquedos,image=bg2)
    label2.place(x=0,y=0,relwidth=1,relheight=1)

    #Entrada de texto bloque dos
    def botonclick(caracter,posi):
        if posi == 1:
            entradanombre0.insert(END,caracter)
            
        elif posi == 2:
            entradanombre1.insert(END,caracter)  

    def cambio(click):
        global posi
        posi= click

    

    entradanombre1=Entry(bloquedos,width=76,border=0,font=('Arial',12),cursor="xterm")
    entradanombre1.place(x=212.1, y=382, width=613, height=20)

    entradanombre0.bind("<FocusIn>",lambda e:cambio(1))
    entradanombre0.bind("<FocusOut>",lambda e:cambio(2))  
    
    #Botones
    #Botones de operaciones aritmeticas
    #Suma
    sumaboton = Button(bloquedos,image=sumaimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('+',posi),cursor="hand2")
    sumaboton.place(x=367,y=416)

    #Resta
    restaboton1 = Button(bloquedos,image=restaimh,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('-',posi),cursor="hand2")
    restaboton1.place(x=405,y=416)

    #Multiplicar
    multboton1 = Button(bloquedos,image=multimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('x',posi),cursor="hand2")
    multboton1.place(x=440,y=416)

    #Division
    divisionboton1 = Button(bloquedos,image=divimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('/',posi),cursor="hand2")
    divisionboton1.place(x=478,y=416)

    #Exponente
    expboton1 = Button(bloquedos,image=expimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('^',posi),cursor="hand2")
    expboton1.place(x=516,y=416)

    #Raiz
    raizboton1 = Button(bloquedos,image=raizimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('√',posi),cursor="hand2")
    raizboton1.place(x=554,y=415)

    #Parentesis abierto
    paropenboton1 = Button(bloquedos,image=paroimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick('(',posi),cursor="hand2")
    paropenboton1.place(x=592,y=416)

    #Parentesis abierto
    parcloseboton1 = Button(bloquedos,image=parcimg,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:botonclick(')',posi),cursor="hand2")
    parcloseboton1.place(x=630,y=416)


    #Boton de ir al menu de opciones-> Solo nos permite dos opciones(Debido a que con dos polinomios solo se puede hacer suma o resta)
    proceder = PhotoImage(file="ico/Siguiente.png")
    procedelabel = Label(image=proceder)
    procedeboton = Button(bloquedos,image=proceder,borderwidth=0,bg="#B9CED9",activebackground='#B9CED9',command=lambda:gonext(2),cursor="hand2")
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

    #Empezamos con el inicio para luego ir cambiando de frames
    bloqueuno.pack(fill='both', expand=1)
    mainpage.mainloop()

#Funcion principal de la interfaz 
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