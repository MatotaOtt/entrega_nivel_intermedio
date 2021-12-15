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
        id_a_eliminar = self.mi_vista.get_id_a_modificar_eliminar()           
        if id_a_eliminar > 0:
            Cuadrodialogo = askquestion(title="Alerta", message="¿Esta seguro que quiere eliminar la tarea con Id: "+str(id_a_eliminar)+" ?")
            if Cuadrodialogo == "yes":
                self.mi_modelo.baja(id_a_eliminar)
            self.listar()
            self.mi_vista.limpiar_id_a_modificar_eliminar()
 
        
  
    def guardar_Modifica(self):
        parametros = self.mi_vista.get_parametros()
        id_a_modificar = self.mi_vista.get_id_a_modificar_eliminar()  #tree.item(self.mi_vista.tree.selection())['values'][0]
        
        Cuadrodialogo= askquestion(title="Alerta", message="¿Esta seguro que quiere modificar el evento seleccionado?")    
        if Cuadrodialogo=="yes":
            self.mi_modelo.modificacion(parametros,id_a_modificar)     
            self.mi_vista.limpiar_filtros()        
            self.mi_vista.deshabilitar_guardar_cancelar_Modificar() 
            self.mi_vista.deshabilitar_entrys()
            self.mi_vista.habilitar_abm() 
            self.listar()       
        else:
            self.mi_vista.cancelar()
        self.mi_vista.limpiar_id_a_modificar_eliminar()
    
    def buscar(self):              ##################################### CORRGIR encapsulamiento
        self.mi_vista.deshabilitar_abm()
        self.mi_vista.habilitar_filtrar_cancelar()
        self.mi_vista.habilitar_entrys()
        self.mi_vista.limpiar_filtros()
        