import random
import sys
import math
from random import randint


def bloqueada (fila,columna):

    if fila == 0 and tablero [fila + 1][columna ]!='':
        fail=True

    elif fila == 1:
         if tablero [fila + 1][columna ]!='' and tablero [fila - 1][columna ]!='':
             fail= True


    elif fila == 2 and tablero [fila - 1][columna] != ' ':
        fail= True
    else:
        fail = False
    return fail

def printertbalero (tablero):
    contador_indice = 0
    for tablero[contador_indice] in tablero:
        print(tablero[contador_indice])
        contador_indice += 1
    print("\n")

def movimiento(fila, columna):
    if fila == 0:
            tablero[fila+1][columna] = tablero[fila][columna]
            tablero[fila][columna] = ' '
    elif fila == 1:
        if tablero[fila+1][columna] != ' ':
            tablero[fila-1][columna] = tablero[fila][columna]
            tablero[fila][columna] = ' '
        else:
            tablero[fila + 1][columna]= tablero [fila][columna]
            tablero [fila][columna] = ' '
    elif fila == 2:
        tablero[fila - 1][columna]= tablero[fila][columna]
        tablero [fila][columna] = ' '

def cambio(fila, columna):
    if fila == 0:
        fila = fila + 1
    elif fila == 1:
        if tablero[fila+1][columna] != ' ':
            fila = fila - 1
        else:
            fila = fila + 1
    elif fila == 2:
        fila = fila - 1
    return fila

while True:
tablero = [
[' ',' ',' '],
[' ',' ',' '],       
[' ',' ',' ']
]

x = randint(0,2)
y = randint(0,2)
z = randint(0,2)
a = randint(0,2)
b = randint(0,2)
c = randint(0,2)