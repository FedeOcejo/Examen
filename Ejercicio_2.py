import random
import sys
import math
from random import randint

tablero = []
for i in range (3):
    tablero.append ( [' '] * 3)

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
    tablero = []
for i in range (3):
    tablero.append ( [' '] * 3)


x = randint(0,2)
y = randint(0,2)
z = randint(0,2)
a = randint(0,2)
b = randint(0,2)
c = randint(0,2)

while x == a:
        a = randint(0,2)
while y == b:
        b = randint(0,2)
while z == c:
        c = randint(0,2)

(tablero[x])[0] = chr(0x2656)
(tablero[y])[1] = chr(0x2656)
(tablero[z])[2] = chr(0x2656)
(tablero[a])[0] = chr(0x265C)
(tablero[b])[1] = chr(0x265C)
(tablero[c])[2] = chr(0x265C)

printertbalero (tablero)

errorx = bloqueada(x, 0)
errory = bloqueada(y, 1)
errorz = bloqueada(z, 2)
errora = bloqueada(a, 0)
errorb = bloqueada(b, 1)
errorc = bloqueada(c, 2)

if errorx == True and errory == True and errorz == True:
        print("El jugador blanco no se puede mover, volvemos a crear el tablero")
        pass
elif errora == True and errorb == True and errorc == True:
        print("El jugador negro no se puede mover, volvemos a crear el tablero")
        pass
else:
        break

turno = randint(0, 1)
while True:
    if turno == 1:
        if errorx == False and errora == False:
            movimiento(x, 0)
            x = cambio(x, 0)
            errora = bloqueada(a, 0)
        elif errory == False and errorb == False:
            movimiento(y, 1)
            y = cambio(y, 1)
            errorb = bloqueada(b, 1)
        elif errorz == False and errorc == False:
            movimiento(z, 2)
            z = cambio(z, 2)
            errorc = bloqueada(c, 2)
        elif errorx == False:
            movimiento(x, 0)
            x = cambio(x, 0)
            errora = bloqueada(a, 0)
        elif errory == False:
            movimiento(y, 1)
            y = cambio(y, 1)
            errorb = bloqueada(b, 1)
        elif errorz == False:
            movimiento(z, 2)
            z = cambio(z, 2)
            errorc = bloqueada(c, 2)
        else:
            break
        turno = 0