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

    else:
            fail=False

    elif fila == 2 and tablero [fila - 1][columna] != ' ':
        fail= True

    else:
        fail = False

    return fail

def printertbalero (tablero):
    contador_indice = 0

while True:

tablero = [
['','',''],
['','',''],       
['','','']
]
