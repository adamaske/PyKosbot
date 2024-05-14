import socket
import json
import time

from PyKosbot.Networking import packet
from PyKosbot.Networking import send_recieve_packets


HOST = "127.0.0.1"
PORT = 8000

options = []
close_command = "q"

if __name__ == "__main__":
    print("Welcome to Kosbot - Python Interface")
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    
    welcome_packet = packet.RecievePacket(client)# TODO : REMOVE 

    running = True
    while(running):
        
        idx = 0
        for option in options:
            print(option)
            
            idx +=1
        
        user_input = input("input : ")
        
    client.close()
    exit()