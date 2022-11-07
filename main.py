from tkinter import Tk, Button, Entry, StringVar

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("525x260")
operecion=""
total=0
reset_pantalla=False

# Configuración pantalla de salida 
numeroPantalla=StringVar()
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"), textvariable=numeroPantalla)
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="W") #Puse 4 y 1

# Configuracion salida por pantalla texto

def numeroPulsado(num):
    global operecion
    global reset_pantalla
    global num1

    if reset_pantalla!=False:
        numeroPantalla.set(num)
        reset_pantalla=False
    else: 
        numeroPantalla.set(numeroPantalla.get()+num)

# Funcion Suma

def suma(num):
    global operecion
    global total
    global reset_pantalla

    total+=int(num)
    operecion= "suma"
    reset_pantalla=True
    numeroPantalla.set(total)

# FUncion Resta

num1=0
contador_resta=0
def resta(num):

	global operecion
	global total
	global num1
	global contador_resta
	global reset_pantalla

	if contador_resta==0:
		num1=int(num)
		total=num1

	else:
		if contador_resta==1:
			total=num1-int(num)
		else:
			total=int(total)-int(num)	
                        
		numeroPantalla.set(total)
		total=numeroPantalla.get()

	contador_resta+=1
	operecion="resta"
	reset_pantalla=True

# Funcion Multiplicacion

contador_multi=0
def multiplica(num):

	global operecion
	global total
	global num1
	global contador_multi
	global reset_pantalla
	
	if contador_multi==0:
		num1=int(num)
		total=num1
	else:
		if contador_multi==1:
			total=num1*int(num)
		else:
			total=int(total)*int(num)	
		numeroPantalla.set(total)
		total=numeroPantalla.get()

	contador_multi+=1
	operecion="multiplicacion"
	reset_pantalla=True

# Funcion Division
	
contador_divi=0
def divide(num):
	global operecion
	global total
	global num1
	global contador_divi
	global reset_pantalla
	
	if contador_divi==0:
		num1=float(num)
		total=num1
	else:
		if contador_divi==1:
			total=num1/float(num)
		else:
			total=float(total)/float(num)	
		numeroPantalla.set(total)
		total=numeroPantalla.get()

	contador_divi+=1
	operecion="division"
	reset_pantalla=True
	
# Funcion igual o elResultado
	
def elResulado():

	global total
	global operecion
	global contador_resta
	global contador_multi
	global contador_divi
	
	if operecion=="suma":
		numeroPantalla.set(total+int(numeroPantalla.get()))
		total=0
	elif operecion=="resta":
		numeroPantalla.set(int(total)-int(numeroPantalla.get()))
		total=0
		contador_resta=0
	elif operecion=="multiplicacion":
		numeroPantalla.set(int(total)*int(numeroPantalla.get()))
		total=0
		contador_multi=0
	elif operecion=="division":
		numeroPantalla.set(int(total)/int(numeroPantalla.get()))
		total=0
		contador_divi=0

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: numeroPulsado("1")).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: numeroPulsado("2")).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: numeroPulsado("3")).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: numeroPulsado("4")).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: numeroPulsado("5")).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: numeroPulsado("6")).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: numeroPulsado("7")).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: numeroPulsado("8")).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda: numeroPulsado("9")).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command=lambda: elResulado()).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command= lambda: suma(numeroPantalla.get())).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command= lambda: resta(numeroPantalla.get())).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command= lambda: multiplica(numeroPantalla.get())).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command= lambda: divide(numeroPantalla.get())).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()