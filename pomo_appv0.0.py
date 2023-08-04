### Esta va a ser la app mas basica, sin GUI, simplemente codigo, para aprender bien la logica de un reloj y su programacion##

import time
import os

#study = input("Cuantos minutos queres estudiar?")
#rest = input("Cuantos minutos  queres descansar?")
#def pomodoro(study, rest):
#    countdown()

#____Con esta funcion convertimos los minutos ingresados por el usuario en segundos. (1/60)____#
def pasar_a_minutos(num):
    return num * 60

#____Con esta funcion restamos el tiempo ingresado hasta llegar a 0. (1/60)____#
def countdown(t):
    while t > 0:
        print (t)
        #time.sleep(x) sirve para esperar x segundo/s entre vuelta y vuelta.
        time.sleep(1)
        t -= 1
    print("SE TERMINO EL TIEMPOOO")

countdown(int(input("cuantos segundos?:")))