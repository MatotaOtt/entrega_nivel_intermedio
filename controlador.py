# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 23:06:31 2021

@author: Francisco Peralta, Matias Ott, Violeta Dorati, Adrian Orellano
"""
from tkinter.messagebox import askquestion
import modelo
import vista
from datetime import datetime, date


class Controlador:
    def __init__(self):
        self.mi_modelo = modelo.Modelo(self)
        self.mi_vista = vista.Vista(self)
        self.listar()
        self.mi_vista.main_loop()

    def listar(self):
        parametros = self.mi_vista.get_parametros()
        self.tabla = self.mi_modelo.get_tareas(parametros)
        self.mi_vista.listar(self.tabla)
        
    def alta(self):
        self.mi_vista.preparar_alta()
        
  
    def guardar(self):
        parametros = self.mi_vista.get_parametros()
        self.mi_modelo.alta(parametros)
        self.mi_vista.limpiar_filtros()
        self.listar()
        self.mi_vista.cerrar_alta()


    def baja(self):
        id_a_eliminar=self.mi_vista.tree.item(self.mi_vista.tree.selection())['values'][0]
        nombre_evento=self.mi_vista.tree.item(self.mi_vista.tree.selection())['values'][1]        
        Cuadrodialogo= askquestion(title="Alerta", message="¿Esta seguro que quiere eliminar este evento con nombre "+str(nombre_evento)+" ?")
        if Cuadrodialogo=="yes":
            self.mi_modelo.baja(id_a_eliminar)
        else:
            pass
        self.listar()
        
    def modificacion(self):
        self.mi_vista.deshabilitar_abm()
        id_a_modificar=self.mi_vista.tree.item(self.mi_vista.tree.selection())['values'][0]
        self.mi_vista.modificar_datos(id_a_modificar)      
        
  
    def guardar_Modifica(self):
        parametros = self.mi_vista.get_parametros()
        id_a_modificar=self.mi_vista.tree.item(self.mi_vista.tree.selection())['values'][0]
        Cuadrodialogo= askquestion(title="Alerta", message="¿Esta seguro que quiere modificar el evento con seleccionado ")    
        if Cuadrodialogo=="yes":
            self.mi_modelo.modificacion(parametros,id_a_modificar)     
            self.mi_vista.limpiar_filtros()        
            self.mi_vista.deshabilitar_guardar_cancelar_Modificar() 
            self.mi_vista.deshabilitar_entrys()
            self.mi_vista.habilitar_abm() 
            self.listar()       
        else:
            self.mi_vista.cancelar()
    
    def buscar(self):
        self.mi_vista.deshabilitar_abm()
        self.mi_vista.habilitar_filtrar_cancelar()
        self.mi_vista.limpiar_filtros()
        self.mi_vista.habilitar_entrys()
        self.mi_vista.hora_desde.config(state="disable") 
        self.mi_vista.minuto_desde.config(state="disable") 
        self.mi_vista.hora_hasta.config(state="disable") 
        self.mi_vista.minuto_hasta.config(state="disable")
        self.mi_vista.e4.config(state="disable")
        self.mi_vista.e7.config(state="disable")        
        self.mi_vista.e8.config(state="disable")
        self.mi_vista.e2.set_date(date.today())
        self.mi_vista.e3.set_date(date.today())
         
        
    def aplicar_filtro(self):
        self.mi_vista.limpiar_tree()
        parametros=self.mi_vista.filtro_Get()
        tabla=self.mi_modelo.aplicar_filtro(parametros)
        
        for fila in tabla:
            self.mi_vista.tree.insert('', 'end', values=(fila[0], fila[1], datetime.fromtimestamp(int(fila[2])).strftime('%d/%m/%Y %H:%M:%S'), datetime.fromtimestamp(int(fila[3])).strftime('%d/%m/%Y %H:%M:%S'), fila[4], fila[5], fila[6], fila[7], fila[8]))
        self.mi_modelo.desconectar_db()   
        
        
        