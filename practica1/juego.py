#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Jugador:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.numeros_propuestos = 0

    def pensar(self):
        if self.tipo == "maquina":
            self.numero_pensado = random.randint(0, 1000)
        else:
            self.numero_pensado = int(input("{} introduce un número pensado (0 .. 1000): ".format(self.nombre)))
        return self.numero_pensado

    def proponer(self):
        self.numeros_propuestos = self.numeros_propuestos + 1
        return int(input("{} introduce un número a ver si lo adivinas: ".format(self.nombre)))

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

class Partida:
    def __init__(self, nombre_j1, nombre_j2, tipo_j2):
        self.jugador1 = Jugador(nombre_j1, "persona")
        self.jugador2 = Jugador(nombre_j2, tipo_j2)
        self.numero_intentos = 0

        self.jugador2.pensar()
        while self.jugador2.comprobar(self.jugador1.proponer()) == 0:
            self.numero_intentos = self.numero_intentos + 1

        print("Partida terminada. Número de intentos: {}".format(self.numero_intentos))


while raw_input("¿Quieres jugar una partida (s/n)? ") == "s":
    partida = Partida(raw_input("Nombre del jugador 1: "), raw_input("Nombre del jugador 2: "), raw_input("¿Jugador 2 es una persona o una maquina?(persona/maquina): "))