import socket

HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'
DISSCONECT_MSG = 'disconnect'
Session=True
SERVER = "0.0.0.0"
ADDR = (SERVER,PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048))

while(Session):    
    string = input("enter the message \n")
    if(string==DISSCONECT_MSG):
        Session = False
    send(string)
    


    
