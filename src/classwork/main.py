import threading
import time

mutex = threading.Lock()

def function(sign : str):
    mutex.acquire()
    for i in range(1, 11):
        print(sign * i)
    print()
    # time.sleep(20)
    for i in range(10, 0, -1):
        print(sign * i)
    mutex.release()

Thr1 = threading.Thread(target=function, args=("#"))
Thr1.daemon = True
Thr1.start()
Thr1 = threading.Thread(target=function, args=("*"))

Thr1.start()

Thr1.join()
# Thr2.join()
