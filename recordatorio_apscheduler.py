from apscheduler.schedulers.background import BackgroundScheduler
import time 

def mostrar_hora():
    print(f"Hora actual: {time.ctime()}")

def recordar_platos():
    print("Recuerda lavar los platos")
    print(f"Hora actual: {time.ctime()}")

def recordar_basura():
    print("Recuerda sacar la basura")
    print(f"Hora actual: {time.ctime()}")

def recordar_comida():
    print("Recuerda cocinar la comida")
    print(f"Hora actual: {time.ctime()}")

scheduler = BackgroundScheduler()
scheduler.add_job(recordar_platos, 'interval', seconds=5)
scheduler.add_job(recordar_basura, 'interval', seconds=8)
scheduler.add_job(recordar_comida, 'interval', seconds=12)
scheduler.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    scheduler.shutdown()