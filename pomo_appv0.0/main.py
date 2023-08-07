#@! Esta va a ser la app mas basica, sin GUI, simplemente codigo, para aprender bien la logica de un reloj y su programacion !@#

#____Importamos los modulos para la aplicacion____#
import time
import os
from playsound import playsound

#____Con esta funcion convertimos los minutos ingresados por el usuario en segundos. (1/60)____#
def pasar_a_minutos(num):
    return num * 60
    
#____Con esta funcion restamos el tiempo ingresado hasta llegar a 0. (1/60)____#
def countdown(t, frame):
    while t > 0:
        if t >= 60:
            min = t // 60
            seg = t - (60 * min)
        else:
            min = 0
            seg = t
        print (f"{frame}:{min}:{seg}")
        #time.sleep(x) sirve para esperar x segundo/s entre vuelta y vuelta.
        time.sleep(1)
        t -= 1
        os.system("cls")

#___Definimos las dos variables para la funcion principal (no me gusta q esten afuera pero bueno)___#
study = int(input("Cuantos minutos queres estudiar?:"))
rest = int(input("Cuantos minutos  queres descansar?:"))

#____FUNCION PRINCIPAL____#
def POMODORO(study, rest):
    t = pasar_a_minutos(study)
    r = pasar_a_minutos(rest)
    os.system("cls")
    countdown(t, frame=("estudia"))
    os.system("cls")
    countdown(r, frame=("descansa"))
    print("TERMINASTE DE ESTUDIAR")
    #____Con esta linea definimos la alarma que va a sonar cuando termine el tiempo____#
    playsound(os.path.join(os.path.dirname(__file__), "./sound/rntn.mp3"))

#___Llamamos a la funcion___#
POMODORO(study, rest)
