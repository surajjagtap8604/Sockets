import socket
import threading
import sys
Buffer = 56 
FORMAT = 'utf-8'

try : 
    SERVER = socket.gethostbyname(socket.gethostname())
except socket.gaierror :
    print("Could not resolve IP address : ")
    sys.exit()
ADDR = (SERVER,5050) # (ipv4,port)
print("server address :", ADDR)
try : 
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err :
    print("Could not create socket : %s"%err)
    sys.exit()

print("creating socket")

server.bind(ADDR)

def client_handle(conn,addr):
    print(F"Connected to {addr}")
    while True:
        msg_len = conn.recv(Buffer).decode(FORMAT)
        if msg_len :
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            if not msg: break
            print(f" {addr} : {msg}")
            
    

def start():
    server.listen()
    print(server)

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client_handle, args=(conn,addr))
        thread.start()
        print(F"Active connection : {threading.active_count() - 1}")
    
print("Server is starting . . . . .")

start()