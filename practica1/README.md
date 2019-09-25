# Práctica 01.- Adivinar un número

He creado la clase Partida de tal manera que se debe inicializar con
el nombre de los jugadores y si el jugador 2 es una persona o una máquina.
Valido esta ultima acción de tal manera que si el usuario no pone "persona"
o "maquina" vuelve a pedir que lo introduzca. La clase partida al inicializarla
aparte de generar los jugadores empieza la partida.

Tambien he creado la constante MAXIMO_NUMERO, que indica el intervalo de
números que se puede escoger para adivinar. En el código propuesto es 100.
Lo he hecho asi, por si en el futuro se quiere cambiar.

La clase Jugador se inicializa con el nombre del jugador y el tipo que es
(persona o maquina). Tenemos el método pensar, que es el encargado de escoger
el número a adivinar. Si el jugador 2 es una máquina este se escoge aleatoriamente
entre 0 y MAXIMO_NUMERO. para ello he tenido que poner la instrución "import random"
para importar la clase random, encargada de generar el número aleatorio. Si el
jugador 2 es una persona entonces este número se pide por teclado, validado que este
sea un entero comprendido entre 0 y MAXIMO_NUMERO. Vuleve a pedirlo de no ser asi.
En el método proponer se le pide al usuario introducir un número, si este no es un valor esperado, se notifica el error y se vuleve a pedir.

Por ultimo decir que he puesto lo siguiente:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```
Esto lo pongo para permitir acentos y demás caracteres que no esten en ASCII