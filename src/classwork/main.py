# Конечные точки - endpoint - это место приема сетевого трафика
#   (интерфейс, ссылка и тд.) на непосредственно той машине,
#   которая будет осуществлять обработку запроса

# Сокет - это абстрактное представление сетевой конечной точки выраженный
#   в конкретном ip адресе и порту

# import socket
#
#
# ipAdress = "127.0.0.1"
# port = 48084 # до 1024 порта запрещено использовать без режима привилегий
#
# soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# soc.bind((ipAdress, port))
# soc.listen(10)
# connective, addr = soc.accept()
# while True:
#     print(f"Установлено новое соединение: {addr}")
#     data = ""
#     dataBinary = connective.recv(1024)
#     if not dataBinary:
#         break
#     data += dataBinary.decode()
#     print(f"Пришли следующие данные: {data}")
#     message = input()
#     if message == "quit":
#         connective.close()
#         break
#     connective.send(message.encode())
#     if not soc:
#         break


#-======- Код клиента - запустить в отдельном окне и проекте -=======-
'''
import socket

ipServer = "127.0.0.1"
port = 48084
sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockClient.connect((ipServer, port))

while True:
    message = input()
    if message == "quit":
        sockClient.close()
        break
    sockClient.send(message.encode())
    data = ""
    # while True:
    dataBinary = sockClient.recv(1024)
    data += dataBinary.decode()
    print(f"Ответ: {data}")
'''
import errno
import threading
import socket
from network.ClientConnection import ClientConnection as ClientCon
__mutexLocker = threading.Lock()

__socketAddr = str()
__socketPort = 0
__socketServer = socket.socket()

__clientDict = dict()



def createServer( address: str, port: int):
    __socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    __socketAddr = address
    __socketPort = port


def SendMessageAll(nameClient: str, message: str):
    __mutexLocker.locked()
    if nameClient in __clientDict:
        for key in __clientDict:
            if key == nameClient:
                continue
            __clientDict[key].addMessageForSending(message)
    else:
        for key in __clientDict:
            if key == "tempNameClient":
                __clientDict[nameClient] = __clientDict["tempNameClient"]
                __clientDict.pop("tempNameClient")
                continue
            else:
                __clientDict[key].addMessageForSending(message)
    __mutexLocker.release()


def Leon(nameClient: str):
    __mutexLocker.locked()
    for key in __clientDict:
        if key != nameClient:
            continue
        __clientDict[nameClient].StopThread()
        __clientDict[nameClient].join()
        __clientDict.pop(nameClient)
        break
    __mutexLocker.release()


def job():
    __socketServer.bind((__socketAddr, __socketPort))
    __socketServer.listen()
    __socketServer.settimeout(5)
    while True:
        try:
            client, addr = __socketServer.accept()
            __clientDict["tempNameClient"] = ClientCon(client, SendMessageAll, Leon)
        except socket.timeout:
            continue
        except OSError as error:
            if error == errno.ETIMEDOUT:
                continue
            else:
                print(error)
                break
        except Exception as error:
            print(error)
            break

    if len(__clientDict):
        for client in __clientDict:
            client.StopThread()
            client.join()
        __clientDict.clear()

    if __socketServer:
        __socketServer.close()


if __name__ == "__main__":
    createServer("127.0.0.1", 48084)
    job()
