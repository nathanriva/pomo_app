#@! Esta va a ser la app mas basica, sin GUI, simplemente codigo, para aprender bien la logica de un reloj y su programacion !@#

#____Importamos los modulos para la aplicacion____#
import time
import os

#____Con esta funcion convertimos los minutos ingresados por el usuario en segundos. (1/60)____#
def pasar_a_minutos(num):
    return num * 60

#def separar_en_minutos(mins=120):
    while 1==1:
        if mins > 60:
            mins // 60
        print(mins)

#____Con esta funcion restamos el tiempo ingresado hasta llegar a 0. (1/60)____#
def countdown(t):
    while t > 0:
        if t >= 60:
            min = t // 60
            seg = t - (60 * min)
        else:
            min = 0
            seg = t
        print (f"{min}:{seg}")
        #time.sleep(x) sirve para esperar x segundo/s entre vuelta y vuelta.
        time.sleep(1)
        t -= 1
        os.system("cls")
    print("SE TERMINO EL TIEMPOOO")

#___Definimos las dos variables para la funcion principal (no me gusta q esten afuera pero bueno)___#
study = int(input("Cuantos minutos queres estudiar?:"))
rest = int(input("Cuantos minutos  queres descansar?:"))

#____FUNCION PRINCIPAL____#
def POMODORO(study, rest):
    t = pasar_a_minutos(study)
    r = pasar_a_minutos(rest)
    countdown(t)
    countdown(r)
    print("TERMINASTE DE ESTUDIAR")
    os.system("clear||cls")

#___Llamamos a la funcion___#
POMODORO(study, rest)
