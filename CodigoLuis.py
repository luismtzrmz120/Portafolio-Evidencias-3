#CodigoLuis.py
#Luis Roberto Martinez Ramirez - A01662619
#Es un proceso donde contiene los 5 pasos, start, ready, running, waiting, finished

import logging 
import threading 
import time

def thread_function(name):
    logging.info("Thread %s: starting", name) 
    time.sleep(2)
    logging.info("Thread %s: finishing", name)
        
if __name__ == "__main__":
   format = "%(asctime)s: %(message)s"
   logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S") 
   logging.info("Main : before CREATING thread")
   x = threading.Thread(target=thread_function, args=(1,))
   y = threading.Thread(target=thread_function, args=(2,))
   logging.info("Main : before RUNNING thread")
   x.start()
   y.start()
   logging.info("Main : wait for the thread to FINISH")
   x.join()
   y.join()
   logging.info("Main : EXIT")
   
#Que es un Thread? es una serie de instrucciones donde es la unidad más pequeña a la cual un procesador le puede asignar tiempo.

#En que orden se esperaba que se imprimiera?
   
#11:31:14: Main : before CREATING thread
#11:31:14: Main : before RUNNING thread
#11:31:14: Thread 1: starting
#11:31:14: Main : wait for the thread to FINISH
#11:31:14: Main : EXIT
#>>> 11:31:16: Thread 1: finishing      
   
#En que orden se imprimio realmente?
   
#11:32:56: Main : before CREATING thread
#11:32:56: Main : before RUNNING thread
#11:32:56: Thread 1: starting
#11:32:56: Thread 2: starting
#11:32:56: Main : wait for the thread to FINISH
#11:32:58: Thread 1: finishing
#11:32:58: Thread 2: finishing
#11:32:58: Main : EXIT
   
#Como cambia el orden de la impresion con la instruccion join() y por que?
#el join cambia la secuencia de la funcion que se esta ejecutando y por eso hace que se imprima más rapido   

#Para que sirve la libreria logging? informa los eventos que ocurren al momento de ejecutar el programa

