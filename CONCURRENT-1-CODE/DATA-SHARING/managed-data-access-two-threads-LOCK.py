import threading
from threading import Thread, Event
from time import time
from time import sleep
from threading import Lock

event = Event()
data_lock = Lock()

def modify_variable(var):
    while True:
        for i in range(len(var)):
            with data_lock:
                var[i] += 1
        if event.is_set():
            break
    print('Stop printing')

my_var = [1, 2, 3]
t = threading.Thread(target=modify_variable, args=(my_var, ))
t2 = threading.Thread(target=modify_variable, args=(my_var, ))
t.start()
t2.start()
t0 = time()

while time()-t0 < 5:
#while True:
    try:
        print(my_var)           
        sleep(1)
    except KeyboardInterrupt:
        event.set()
        break
event.set()
t.join()
t2.join()
print(my_var)
