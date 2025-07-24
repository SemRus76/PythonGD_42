import time
import psycopg2
import threading

class DataBaseInterface(threading.Thread):

    # __connectDb = "connection"
    # __cursorDB = "cursor"
    __ThreadStop = False
    __mutexLocker = threading.Lock()

    __results = str()
    __resReady = False

    # Флаги обращения
    __select = False

    def StopThread(self):
        self.__ThreadStop = True

    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self)
        self.__connectDb = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="123",
            host="localhost",
            port=5432
        )
        self.__cursorDB = self.__connectDb.cursor()

    def __del__(self):
        self.__connectDb.close()

    def run(self) -> int:
        while True:
            if self.__ThreadStop:
                break
            if self.__select:
                query = "SELECT id, name, age FROM public.example;"
                self.__cursorDB.execute(query)

                res = self.__cursorDB.fetchall()
                self.__results = ""
                self.__results = "id\t\tname\t\tage\n"
                for line in res:
                    for elem in line:
                        self.__results+= f"{elem}\t\t"
                    self.__results+="\n"
                self.__select = False
                self.__resReady = True
            else:
                time.sleep(0.5)

        return 0

    def getSelect(self) -> bool:
        self.__mutexLocker.acquire()
        if self.__select:
            self.__mutexLocker.release()
            return False
        self.__select = True
        self.__mutexLocker.release()
        return True

    def statusResult(self) -> bool:
        return self.__resReady

    def getResult(self) -> str:
        self.__mutexLocker.acquire()
        if not self.__resReady:
            self.__mutexLocker.release()
            return str()
        self.__resReady = False
        self.__mutexLocker.release()
        if not self.__results:
            return "not results"
        return self.__results

