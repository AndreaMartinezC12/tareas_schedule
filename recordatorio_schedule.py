import schedule
import time

def tarea():
    print("tarea ejecutada")

def tareasimprimir(nombre_tarea):
    print(nombre_tarea)


tiempos = []
tareas = input('Cuales tareas deseas agregar?')
tareasind = tareas.split(",")

for i in range (0, len(tareasind)):
    tiempoind = int(input(f'Cada cuando debo recordar {tareasind[i]}  en segundos?'))
    schedule.every(tiempoind).seconds.do(tareasimprimir, tareasind[i])

while True:
    schedule.run_pending()
    time.sleep(1)