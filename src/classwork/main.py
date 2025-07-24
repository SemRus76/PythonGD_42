import ThreadingExample.DataBaseInterface as DataBaseInter
# import psycopg2
# import threading
import time


DBThread = DataBaseInter.DataBaseInterface()
DBThread.start()
print("-=============-")

DBThread.getSelect()
while not DBThread.statusResult():
    time.sleep(0.01)
print(DBThread.getResult())
print("-=============-")
# print(count)

DBThread.StopThread()
DBThread.join()



