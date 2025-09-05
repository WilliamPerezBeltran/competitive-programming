# -*- coding: utf-8 -*-
from functools import reduce
from function_time import FunctionTime 


#  Write a function that takes a sentence and returns the longest word.
class LongestWord():

    @FunctionTime.decorator 
    def method_1(self,sentence):
        mayor_len = 0   
        mayor = None    
        for x in sentence.split():
            if len(x) > mayor_len:
                mayor_len = len(x)
                mayor = x
        return  mayor

    @FunctionTime.decorator 
    def method_2(self,sentence):
        mayor = max([(len(x),x) for x in sentence.split()])
        return  mayor[1]
    
    @FunctionTime.decorator 
    def method_3(self,sentence):
        return max(sentence.split(),key=len)
#--------------------------------------------------
#                         CONCEPTO 
#--------------------------------------------------

#    Un generador es un objecto que produce valores uno a uno. 
#    hay dos formas pricipales de creción:
#        1. Con una expresion generadora -> Es una construción de python de la forma 
#           (x for x in iterable)
#        2. Con una funcion generadora -> función que usa yield para generar valores 
#           o devolver valores.Se llama función generadora a cualquier bloque 
#           de codigo que produce valores secuenciales bajo demanda mediante 
#           la palabra yield 
#

    @FunctionTime.decorator 
    def method_4(self,sentence):
        return max((word for word in sentence.split()),key=len)
#--------------------------------------------------
#                         CONCEPTO 
#--------------------------------------------------


#    - Un lambda es un funcion especial o tambien llamada funcion anonima que no tiene 
#                identificar para ser invocado.
#                sintaxis -> lambda parámetro:expresión 
#   
#    - reduce es un concepto funcional que se utiliza para reducir la combinacion de los
#                elementos  a un solo valor.
#    
#                Es decir el concepto de reduccion es el proceso de combinar los elementos de una 
#                colección (lista.arreglo, etc) en un solo valor. 
#    
#                sintaxis:  reduce(funcion,valor, inicial)
    
    @FunctionTime.decorator 
    def method_5(self,sentence):
        return reduce(lambda a,b: a if len(a) > len(b) else b, sentence.split()) 
        
        

