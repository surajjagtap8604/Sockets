import socket 
FORMAT = 'utf-8'
Buffer = 56 
server_addr  = "xxx.xxx.x.x" #write ip address of server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (server_addr,5050)

client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    print(send_length)
    send_length += b' ' * (Buffer - len(send_length))
    print(send_length)
    client.send(send_length)
    client.send(message)
    server_msg = client.recv(1024).decode(FORMAT)
    print(server_msg)
    client.close()
    
send("hello1")