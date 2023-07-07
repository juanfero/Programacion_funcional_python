import time

imprimir_reloj = lambda h, m, s: (lambda: print(f"{h:02d}:{m:02d}:{s:02d}") or time.sleep(1)) 
# se crea funcion lamnda que tiene como argumento 3 parametros: hora, minuto y segundos
# se utiliza time.sleep(1) para pausar la ejecución del programa durante 1 segundo.

h, m, s = 0, 0, 0

while h < 24:
    imprimir_reloj(h, m, s)()
    s = (s + 1) % 60 #empieza a contar los segundos,se utiliza el modulo pra que cuando llegue a 60, se le incremente 1 minuto
    if s == 0:
        m = (m + 1) % 60
        if m == 0:
            h = (h + 1) % 24
# el bucle hace el mismo proceso simpre hasa que llegue a los 24 horas 


