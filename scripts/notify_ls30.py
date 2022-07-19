import socket
import time

sock = socket.socket(socket.AF_INET,
        socket.SOCK_DGRAM)     

UDP_IP = "172.20.0.12" #Target IP Address
UDP_PORT = 30704

#Create a socket    
def sendPacket(MESSAGE):
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT)) #Send message to UDP port

if __name__ == '__main__':
    # Set direction (1=output)
    sendPacket(b'\x19\x07\x00\x00\x00\x07\x00\x00\x00')
    time.sleep(0.5)
    # Set active high
    sendPacket(b'\x1a\x07\x00\x00\x00\x00\x00\x00\x00')
    time.sleep(0.5)
    # Set state inactive first
    sendPacket(b'\x1b\x07\x00\x00\x00\x00\x00\x00\x00')
    time.sleep(0.5)
    # Set state active to signal
    sendPacket(b'\x1b\x01\x00\x00\x00\x01\x00\x00\x00')
    time.sleep(0.5)
    # Set state to inactive again
    sendPacket(b'\x1b\x01\x00\x00\x00\x00\x00\x00\x00')
