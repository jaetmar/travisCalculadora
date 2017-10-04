# -*- coding: utf-8 -*-
from lettuce import step, world
from calculadora import Calculadora

@step(u'cuando realizo la operación')
def cuando_realizo_la_operacion(step):
    pass

@step(u'Dado que ingreso los números "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.sumar(int(num1), int(num2))

@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, res):
    obtenido = world.cal.obtener_resultado()
    try:
        assert float(res) == obtenido, 'El resultado esperado es de ' + res + ' y el obtenido es ' + str(obtenido)
    except ValueError:
         assert res == obtenido, 'El resultado esperado es de ' + res + ' y el obtenido es ' + str(obtenido)
    

@step(u'Dado que ingreso los números de resta "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_de_resta_group1_y_group1(step, num1, num2):
    world.cal = Calculadora()
    world.cal.restar(int(num1), int(num2))

@step(u'Dado que ingreso los números de multiplicacion "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_de_multiplicacion_group1_y_group1(step, num1, num2):
    world.cal = Calculadora()
    world.cal.multiplicar(int(num1), int(num2))

@step(u'Dado que ingreso los números de divison "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_de_divison_group1_y_group1(step, num1, num2):
    world.cal = Calculadora()
    world.cal.dividir(float(num1), float(num2))

@step(u'Dado que ingreso los números de potencia "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_de_potencia_group1_y_group1(step, num1, num2):
    world.cal = Calculadora()
    world.cal.potencia(int(num1), int(num2))

@step(u'Dado que ingreso los números de raiz "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_de_raiz_group1_y_group1(step, num1, num2):
    world.cal = Calculadora()
    world.cal.raiz(int(num1), int(num2))
