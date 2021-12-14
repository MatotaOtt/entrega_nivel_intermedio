# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 23:06:31 2021

@author: Francisco Peralta, Matias Ott, Violeta Dorati, Adrian Orellano
"""
from tkinter.messagebox import askquestion
import modelo
import vista


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
    
    def buscar(self): a=0
    def aplicar_filtro(self): a=0