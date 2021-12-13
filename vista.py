# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 21:59:02 2021

@author: Francisco Peralta, Matias Ott, Violeta Dorati, Adrian Orellano
"""
from tkinter import Tk, Label, Entry, Button, ttk, StringVar, Spinbox, Frame, messagebox
from tkinter.messagebox import askokcancel, WARNING, showinfo
from tkcalendar import DateEntry
from tkinter.ttk import Combobox
import time
from datetime import datetime, date

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador
        ### Ventana 
        self.ventana1 = Tk() #crear la ventana en variable ventana1
        self.ventana1.geometry("620x350")
        self.ventana1.title("Virtual Schedulle")
        
        ### Labels
        self.label1 = Label(self.ventana1, text = "Título:") #crea la etiqueta
        self.label2 = Label(self.ventana1, text = "Fecha y Hora Desde:") #crea la etiqueta
        self.label3 = Label(self.ventana1, text = "Fecha_hora_hasta:") #crea la etiqueta
        self.label4 = Label(self.ventana1, text = "Nota:") #crea la etiqueta
        self.label5 = Label(self.ventana1, text = "Telefono de Contacto:") #crea la etiqueta
        self.label6 = Label(self.ventana1, text = "Tipo:") #crea la etiqueta
        self.label7 = Label(self.ventana1, text = "Unidad:") #crea la etiqueta
        self.label8 = Label(self.ventana1, text = "Recordar Cada:") #crea la etiqueta
        self.label1.grid(row=1, column=0, sticky = "E") #ubicacion
        self.label2.grid(row=2, column=0, sticky = "E") #ubicacion
        self.label3.grid(row=3, column=0, sticky = "E") #ubicacion
        self.label4.grid(row=4, column=0, sticky = "E") #ubicacion
        self.label5.grid(row=1, column=2, sticky = "E") #ubicacion
        self.label6.grid(row=2, column=2, sticky = "E") #ubicacion
        self.label7.grid(row=4, column=2, sticky = "E") #ubicacion
        self.label8.grid(row=3, column=2, sticky = "E") #ubicacion
        
        ### Entrys
        self.e1 = Entry(self.ventana1) #crea entry1 
        self.f1 = Frame(self.ventana1) #crea entry1 
        self.f1.grid(row=2, column=1, sticky = "W") #crea Frame para la fecha y hora desde
        self.f2 = Frame(self.ventana1) #crea Frame para la fecha y hora hasta
        self.e2 = DateEntry(self.f1, width=12, background='darkblue', foreground='white', borderwidth=2,date_pattern='dd/mm/Y')
        self.hourstr_desde = StringVar() #variable de hora
        self.hora_desde = Spinbox(self.f1,from_=0,to=23,wrap=True,textvariable=self.hourstr_desde,width=2,state="readonly") # spinbox de hora
        self.minstr_desde = StringVar() #variable minuto
        self.minuto_desde = Spinbox(self.f1,from_=0,to=59,wrap=True,textvariable=self.minstr_desde,width=2,state="readonly") #spinbox de minuto
        self.e3 = DateEntry(self.f2, width=12, background='darkblue', foreground='white', borderwidth=2,date_pattern='dd/mm/Y')
        self.hourstr_hasta = StringVar()
        self.hora_hasta = Spinbox(self.f2,from_=0,to=23,wrap=True,textvariable=self.hourstr_hasta,width=2,state="readonly")
        self.minstr_hasta = StringVar()
        self.minuto_hasta = Spinbox(self.f2,from_=0,to=59,wrap=True,textvariable=self.minstr_hasta,width=2,state="readonly")
        self.e4 = Entry(self.ventana1) #crea entry
        self.e5 = Entry(self.ventana1) #crea entry 
        self.e6_sv = StringVar() #crea una variable asociada a e6
       # self.e6_sv.trace("w", self.evento_modificacion_entry(self.e6_sv)) #establecre que funcion ejecutar cuando se da el evento de cambio de texto en la variable
        self.e6 = Combobox(self.ventana1, textvariable=self.e6_sv, values=["Tarea", "Evento", "Objetivo"]) #crea el entry pero ademasa le asocia la variable de texto para que el evento detecte el cambio
        self.e8 = Entry(self.ventana1) #crea entry1
        self.e7 = Combobox(self.ventana1, values=["Dias", "Semanas", "Meses"])
        self.f2.grid(row=3, column=1, sticky = "W") 
        self.e1.grid(row=1, column=1, sticky = "W") #ubico adentro de la ventana
        self.e2.grid(row=1, column=0, sticky = "W") #ubico adentro de la ventana
        self.e3.grid(row=1, column=0, sticky = "W") #ubico adentro de la ventana
        self.e4.grid(row=4, column=1, sticky = "W") #ubico adentro de la ventana
        self.e5.grid(row=1, column=3, sticky = "W") #ubico adentro de la ventana
        self.e6.grid(row=2, column=3, sticky = "W") #ubico adentro de la ventana
        self.e8.grid(row=3, column=3, sticky = "W") #ubico adentro de la ventana
        self.e7.grid(row=4, column=3, sticky = "W") #ubico adentro de la ventana
        self.minuto_desde.grid(row=1, column=2,sticky = "EWNS") #ubico adentro de la ventana
        self.hora_desde.grid(row=1, column=1,sticky = "EWNS") #ubico adentro de la ventana
        self.minuto_hasta.grid(row=1, column=2,sticky = "EWNS") #ubico adentro de la ventana
        self.hora_hasta.grid(row=1, column=1,sticky = "EWNS") #ubico adentro de la ventana
        
        ### Botones
        self.boton1 = Button(self.ventana1, text ="Agregar", command = controlador.alta)
        self.boton2 = Button(self.ventana1, text ="Eliminar", command = controlador.baja)
        self.boton3 = Button(self.ventana1, text ="Modificar", command = controlador.modificacion)
        self.boton4 = Button(self.ventana1, text ="Buscar", command = controlador.buscar)
        self.boton5 = Button(self.ventana1, text ="Guardar", command = controlador.guardar)
        self.boton6 = Button(self.ventana1, text ="Cancelar", command = self.cancelar)
        self.boton7 = Button(self.ventana1, text ="Aplicar Filtro", command = controlador.aplicar_filtro)
        self.boton8 = Button(self.ventana1, text ="Cancelar", command = self.cancelar)
        self.boton9 = Button(self.ventana1, text ="Limpiar Filtros", command = self.limpiar_filtros)
        self.boton1.grid(row=5, column=0,sticky = "EWNS") #ubico adentro de la ventana
        self.boton2.grid(row=5, column=1,sticky = "EWNS") #ubico adentro de la ventana
        self.boton3.grid(row=5, column=2,sticky = "EWNS") #ubico adentro de la ventana
        self.boton4.grid(row=5, column=3,sticky = "EWNS") #ubico adentro de la ventana
        self.boton5.grid(row=6, column=2,sticky = "EWNS") #ubico adentro de la ventana
        self.boton6.grid(row=6, column=3,sticky = "EWNS") #ubico adentro de la ventana
        self.boton7.grid(row=6, column=2,sticky = "EWNS") #ubico adentro de la ventana
        self.boton8.grid(row=6, column=3,sticky = "EWNS") #ubico adentro de la ventana
        self.boton9.grid(row=6, column=0,sticky = "EWNS") #ubico adentro de la ventana
        
        ### Listado
        self.tree = ttk.Treeview(self.ventana1, column=("column1","column2", "column3", "column4", "column5", "column6", "column7", "column8", "column9"), show='headings')
        self.tree.heading("#1", text="Id")
        self.tree.heading("#2", text="Titulo")
        self.tree.heading("#3", text="Desde")
        self.tree.heading("#4", text="Hasta")
        self.tree.heading("#5", text="Notas")
        self.tree.heading("#6", text="Contacto")
        self.tree.heading("#7", text="Tipo")
        self.tree.heading("#8", text="D/S/M")
        self.tree.heading("#9", text="Alarma")
        self.tree.column("#1", minwidth=0, width=20, stretch="NO")
        self.tree.column("#2", minwidth=0, width=117, stretch="NO")
        self.tree.column("#3", minwidth=0, width=111, stretch="NO")
        self.tree.column("#4", minwidth=0, width=111, stretch="NO")
        self.tree.column("#5", minwidth=0, width=40, stretch="NO")
        self.tree.column("#6", minwidth=0, width=58, stretch="NO")
        self.tree.column("#7", minwidth=0, width=40, stretch="NO")
        self.tree.column("#8", minwidth=0, width=50, stretch="NO")
        self.tree.column("#9", minwidth=0, width=50, stretch="NO")
        self.tree.grid(row=7,column=0,columnspan=4, sticky='nsew') #ubico adentro de la ventana
        
		### Scroll Bar
        self.vsb = ttk.Scrollbar(self.ventana1, orient="vertical", command=self.tree.yview)
        self.vsb.grid(row=7,column=5,sticky = "EWNS")
        self.tree.configure(yscrollcommand=self.vsb.set)
        
        ### muestra la ventana
        self.deshabilitar_guardar_cancelar()
        self.deshabilitar_filtrar_cancelar()
        self.limpiar_filtros()
        self.deshabilitar_entrys()
        
    def main_loop(self):    
        self.ventana1.mainloop()

    def evento_modificacion_entry(self, sv): #este evento habilita o deshabilita los ultimos 2 entrys dependiendo de si es objetivo o no
        if self.e6.get() == 'Objetivo':
            self.e7.config(state='normal')
            self.e8.config(state='normal')
        else:
            self.e7.current(0)
            self.e7.config(state='disable')
            self.e8.delete(0,'end')
            self.e8.insert(0,'0')
            self.e8.config(state='disable')
                    
    def listar(self, tabla):
        self.limpiar_tree()
        for fila in tabla:
            #print(fila)
            self.tree.insert('', 'end', values=(fila[0], fila[1], datetime.fromtimestamp(int(fila[2])).strftime('%d/%m/%Y %H:%M:%S'), datetime.fromtimestamp(int(fila[3])).strftime('%d/%m/%Y %H:%M:%S'), fila[4], fila[5], fila[6], fila[7], fila[8]))
            
    
     
    def grid_hide(self, widget):
      widget._grid_info = widget.grid_info()
      widget.grid_remove()        
      
      
    def deshabilitar_entrys(self):
        self.e1.config(state="disable")
        self.e2.config(state="disable")
        self.e3.config(state="disable")
        self.e4.config(state="disable")
        self.e5.config(state="disable")
        self.e6.config(state="disable")
        self.e7.config(state="disable")
        self.e8.config(state="disable") 
        self.hora_desde.config(state="disable") 
        self.minuto_desde.config(state="disable") 
        self.hora_hasta.config(state="disable") 
        self.minuto_hasta.config(state="disable") 
        
    def habilitar_entrys(self):
        self.e1.config(state="normal")
        self.e2.config(state="normal")
        self.e3.config(state="normal")
        self.e4.config(state="normal")
        self.e5.config(state="normal")
        self.e6.config(state="normal")
        self.e7.config(state="normal")
        self.e8.config(state="normal") 
        self.hora_desde.config(state="normal") 
        self.minuto_desde.config(state="normal") 
        self.hora_hasta.config(state="normal") 
        self.minuto_hasta.config(state="normal") 
        self.e1.focus()
        
    def habilitar_abm(self):
        self.boton1.grid(row=5, column=0,sticky = "EWNS") #ubico adentro de la ventana
        self.boton2.grid(row=5, column=1,sticky = "EWNS") #ubico adentro de la ventana
        self.boton3.grid(row=5, column=2,sticky = "EWNS") #ubico adentro de la ventana
        self.boton4.grid(row=5, column=3,sticky = "EWNS") #ubico adentro de la ventana
        
    def deshabilitar_abm(self):
        self.grid_hide(self.boton1)
        self.grid_hide(self.boton2)
        self.grid_hide(self.boton3)
        self.grid_hide(self.boton4)

        
    def deshabilitar_filtrar_cancelar(self):
        self.boton7.config(state = "disable")
        self.boton8.config(state = "disable")
        self.boton9.config(state = "disable")    
        self.grid_hide(self.boton7)
        self.grid_hide(self.boton8)
        self.grid_hide(self.boton9)      
                    
        
    def deshabilitar_guardar_cancelar(self):
        self.boton5.config(state = "disable")
        self.boton6.config(state = "disable")
        self.grid_hide(self.boton5)
        self.grid_hide(self.boton6)
    
        
    def habilitar_guardar_cancelar(self):
        self.boton5.grid()
        self.boton6.grid()
        self.boton5.config(state = "normal")
        self.boton6.config(state = "normal")
        

    def habilitar_filtrar_cancelar(self):
        self.boton7.grid()
        self.boton8.grid()
        self.boton9.grid()
        self.boton7.config(state = "normal")
        self.boton8.config(state = "normal")
        self.boton9.config(state = "normal")
    

    def limpiar_entrys(self):
        self.e1.delete(0, 'end')
        self.e2.delete(0, 'end')
        self.e3.delete(0, 'end')
        self.e4.delete(0, 'end')
        self.e5.delete(0, 'end')
        self.e6.delete(0, 'end')
        self.e7.delete(0, 'end')
        self.e8.delete(0, 'end')
        self.e6.current(0)
        self.e7.current(0)
        self.e8.insert(0,'0')
        self.hora_desde.delete(0, 'end')
        self.minuto_desde.delete(0, 'end')
        self.hora_hasta.delete(0, 'end')
        self.minuto_hasta.delete(0, 'end')
        self.hora_desde.insert(0,0)
        self.minuto_desde.insert(0,0)
        self.hora_hasta.insert(0,0)
        self.minuto_hasta.insert(0,0)
        self.e2.set_date(date.today())
        self.e3.set_date(date.today())
    
    def limpiar_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)      
            
            
            
    def cancelar(self):
        self.answer = askokcancel(title='Confirmacion', message='''Esta seguro de Cancelar esta acción? Se perderan los datos ingresados.''', icon=WARNING)
        if self.answer:
            self.habilitar_abm()
            self.limpiar_filtros()            
            self.deshabilitar_guardar_cancelar()
            #self.limpiar_entrys()
            self.deshabilitar_entrys()
            self.deshabilitar_filtrar_cancelar()
            self.controlador.listar()
    
    def limpiar_filtros(self):
        self.limpiar_entrys()
        #self.habilitar_filtrar_cancelar()
        self.e2.delete(0,'end')
        self.e2.insert(0,"01/01/1970")
        self.hora_desde.insert(0,"0")
        self.minuto_desde.insert(0,"0")
        self.e3.delete(0,'end')
        self.e3.insert(0,"01/01/2121")
        self.hora_hasta.insert(0,"0")
        self.minuto_hasta.insert(0,"0")
        self.e6.delete(0,'end')
        self.e7.config(state="normal")
        self.e8.config(state="normal") 
        self.e7.delete(0,'end')
        self.e8.delete(0,'end')
       
   
    def get_parametros(self):
        self.hora_desde_formato_completo = self.hora_desde.get() + ":" + self.minuto_desde.get() + ":00" 
        self.hora_hasta_formato_completo = self.hora_hasta.get() + ":" + self.minuto_hasta.get() + ":00" 
        self.fecha1_timestamp = str(time.mktime(datetime.strptime(str(self.e2.get_date())+ " " + self.hora_desde_formato_completo, "%Y-%m-%d %H:%M:%S").timetuple()))
        self.fecha2_timestamp = str(time.mktime(datetime.strptime(str(self.e3.get_date())+ " " + self.hora_hasta_formato_completo, "%Y-%m-%d %H:%M:%S").timetuple()))
        return (self.e1.get(), int(float(self.fecha1_timestamp)), int(float(self.fecha2_timestamp)), self.e4.get(), self.e5.get(), self.e6.get(), self.e7.get(), self.e8.get())
    
    def preparar_alta(self):
       self.habilitar_entrys()
       self.limpiar_entrys()
       self.habilitar_guardar_cancelar()
       self.deshabilitar_abm()

    def cerrar_alta(self):
        showinfo(title="Alta", message="Se dio de alta una nueva Tarea")
        self.id_ultima_fila = self.tree.get_children()[-1]
        self.tree.focus(self.id_ultima_fila)
        self.tree.selection_set(self.id_ultima_fila)
        self.tree.yview_moveto(1)
        self.habilitar_abm()
        self.deshabilitar_guardar_cancelar()
        self.limpiar_entrys()
        self.deshabilitar_entrys()