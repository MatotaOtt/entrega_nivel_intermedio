# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 23:06:31 2021

@author: Francisco Peralta, Matias Ott, Violeta Dorati, Adrian Orellano
"""
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


    def baja          (self): a=0
    def modificacion  (self): a=0
    def buscar        (self): a=0
    def aplicar_filtro(self): a=0