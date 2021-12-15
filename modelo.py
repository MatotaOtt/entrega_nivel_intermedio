# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 21:59:15 2021

@author: Francisco Peralta, Matias Ott, Violeta Dorati, Adrian Orellano
"""

import sqlite3


class Modelo:
    def __init__(self, controlador):
        self.con = sqlite3.connect('tareas.db')
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS tareas (
            id_tarea integer PRIMARY KEY AUTOINCREMENT, 
            titulo text,
            fecha_hora_desde integer, 
            fecha_hora_hasta integer, 
            nota text, 
            contacto text, 
            tipo text, 
            recordar_cada_tipo text, 
            recordar_cada_cantidad integer)''')
        self.con.commit()
        self.desconectar_db()
    
    def conectar_db(self):
        self.con = sqlite3.connect('tareas.db')
        self.cur = self.con.cursor()
        
    def desconectar_db(self):
        self.con.close()

    def limpiar_db(self):
        self.conectar_db()
        self.cur.execute('''drop table tareas''')
        self.con.commit()
        self.desconectar_db()

    def alta(self, parametros): #titulo, fecha_hora_desde, fecha_hora_hasta, nota, contacto, tipo, recordar_cada_tipo, recordar_cada_cantidad):    
        self.conectar_db()
        self.cur.execute('''INSERT INTO tareas (titulo, fecha_hora_desde, fecha_hora_hasta, nota, contacto, tipo, recordar_cada_tipo, recordar_cada_cantidad ) VALUES (?,?,?,?,?,?,?,?)''', parametros) #titulo,int(fecha_hora_desde), int(fecha_hora_hasta), nota, contacto, tipo, recordar_cada_tipo, int(recordar_cada_cantidad)))
        self.con.commit()
        self.desconectar_db()
    
    def baja(self,id_a_eliminar):
        self.conectar_db()
        self.cur.execute('''DELETE FROM tareas WHERE id_tarea = ? ''', (id_a_eliminar,) )
        self.con.commit()
        self.desconectar_db()
        
    
    def modificacion(self,parametros,id):        
        self.conectar_db()           
        self.cur.execute('''UPDATE tareas SET  titulo = ?, fecha_hora_desde = ?, fecha_hora_hasta = ?, nota = ?, contacto = ?, tipo = ?, recordar_cada_tipo = ?, recordar_cada_cantidad = ? WHERE id_tarea = ?''',(parametros[0],int(parametros[1]), int(parametros[2]), parametros[3], parametros[4], parametros[5], parametros[6], int(parametros[7]),id))
        self.con.commit()
        self.desconectar_db()        
        
    def get_tareas(self,parametros): #id_a_modificar, titulo, fecha_hora_desde, fecha_hora_hasta, nota, contacto, tipo, recordar_cada_tipo, recordar_cada_cantidad):
        nuevos_parametros = []
        #print(parametros)
        self.conectar_db()
        for elemento in parametros:
            if isinstance(elemento, str):
                elemento = "%" + elemento + "%"
            nuevos_parametros.append(elemento)    
        tabla = self.cur.execute('''SELECT * FROM tareas where titulo like ? AND fecha_hora_desde >= ? AND fecha_hora_hasta <= ? AND nota like ? AND contacto like ? AND tipo like ? AND recordar_cada_tipo like ? AND CAST(recordar_cada_cantidad as CHAR) like ? order by id_tarea asc''', tuple(nuevos_parametros) ) #(titulo,int(fecha_hora_desde), int(fecha_hora_hasta), nota, contacto, tipo, recordar_cada_tipo, int(recordar_cada_cantidad), int(id_a_modificar)))
        return tabla
        self.desconectar_db()        


         
        
        