from threading import Thread, Event
from time import sleep
from time import time

event = Event()

def modify_variable(var):
    while True:
        for i in range(len(var)):
            var[i] += 1
        if event.is_set():
            break
    print('Stop printing')


my_var = [1, 2, 3]
t = Thread(target=modify_variable, args=(my_var, ))
t.start()
t0 = time()
while time()-t0 < 5:
    try:
        print(my_var)
        sleep(1)
    except KeyboardInterrupt:
        event.set()
        break
event.set()
t.join()
print(my_var)
