import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 6789))

s.listen(5)
connected = False

while True:
    if connected != True:
        try:
            (clientsoc, addres) = s.accept()
            print("client connected")
            connected = True
        except:
            print("Erm you messed up")

    command = input("Type rickroll To rickroll target, type target to see target info: ")
    if command == "target":
        print(addres)
    if command == "rickroll":
        print("ignor the crash and the error it just needs to send A msg it will rickroll still")
        s.send(command)
        print("rickrolling")
