import socket
import json
import time
import packet

HOST = "127.0.0.1"
PORT = 8000

max_buffer_size = 2048

string_packet_size_byte_amount = 4 #Before a packet is received, the size of it is sent in 2 bytes

packet_type_byte_amount = 4 #The type is descirbed in a 4 byte integer 

def RecievePacket(sock=socket):
    packet_size_bytes = sock.recv(packet.incoming_packet_size_byte_amount)
    packet_size = packet.ParseIncomingPacketSize(packet_size_bytes)
    print("incoming packet size : ", packet_size)
    
    packet_bytes = sock.recv(packet_size)
    print("packet bytes :", packet_bytes)
    type, size, content = packet.ParsePacket(packet_bytes)
    
def SendPacket(sock=socket):
    packet_bytes = packet.MakeStringPacket("Hello from Client!")

    packet_size = int.to_bytes(len(packet_bytes), packet.incoming_packet_size_byte_amount)
    
    sent = sock.send(packet_size)
    sent = sock.send(packet_bytes)
    
    print("Packet size sent ", sent, " bytes")
    print("Packet content sent ", sent, " bytes")
    return
