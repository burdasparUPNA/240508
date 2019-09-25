#!/usr/bin/env python
# -*- coding: utf-8 -*-

MAXIMO_NUMERO = 100

import random

class Jugador:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.numeros_propuestos = 0

    def pensar(self):
        if self.tipo == "maquina":
            self.numero_pensado = random.randint(0, MAXIMO_NUMERO)
        else:
            inputVariable2 = input("{} introduce un número pensado (0 .. {}): ".format(self.nombre, MAXIMO_NUMERO))
            while not(self.validarNumero(inputVariable2)):
                inputVariable2 = input("{} introduce un número pensado (0 .. {}): ".format(self.nombre, MAXIMO_NUMERO))
            self.numero_pensado = int(inputVariable2)
        return self.numero_pensado

    def proponer(self):
        self.numeros_propuestos = self.numeros_propuestos + 1
        inputVariable3 = input("{} introduce un número a ver si lo adivinas (0..{}): ".format(self.nombre, MAXIMO_NUMERO))
        while not(self.validarNumero(inputVariable3)):
            inputVariable3 = input("{} introduce un número a ver si lo adivinas (0..{}): ".format(self.nombre, MAXIMO_NUMERO))
        return int(inputVariable3)

    def comprobar(self, numero_a_comprobar):
        if  numero_a_comprobar == self.numero_pensado:
            print("{} dice has acertado".format(self.nombre))
            return 1
        else:
            if numero_a_comprobar > self.numero_pensado:
                print("{} dice: el número pensado es menor que el propuesto".format(self.nombre))
            else:
                print("{} dice: el número pensado es mayor que el propuesto".format(self.nombre))
            return 0

    def validarNumero(self, numero):
        try:
            if int(numero) < 0 or int(numero) > MAXIMO_NUMERO:
                print("Valor fuera del rango. Introduce un entero comprendido entre 0 .. {}".format(MAXIMO_NUMERO))
                return False
            else:
                return True
        except ValueError:
            print("No valen valores distintos de un entero. Introduce un entero comprendido entre 0 .. {}".format(MAXIMO_NUMERO))
            return False

class Partida:
    def __init__(self, nombre_j1, nombre_j2, tipo_j2):
        self.jugador1 = Jugador(nombre_j1, "persona")
        self.jugador2 = Jugador(nombre_j2, tipo_j2)
        self.numero_intentos = 0

        self.jugador2.pensar()
        while self.jugador2.comprobar(self.jugador1.proponer()) == 0:
            self.numero_intentos = self.numero_intentos + 1

        print("Partida terminada. Número de intentos: {}".format(self.numero_intentos))


while input("¿Quieres jugar una partida (s/n)? ") == "s":
    inputVariable = input("¿Jugador 2 es una persona o una maquina?(persona/maquina): ")
    while inputVariable != "persona" and inputVariable != "maquina":
        print("Valor no válido")
        inputVariable = input("¿Jugador 2 es una persona o una maquina?(persona/maquina): ")
    partida = Partida(input("Nombre del jugador 1: "), input("Nombre del jugador 2: "), inputVariable)