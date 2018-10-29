import socket

host = '127.0.0.1'
port = 5001

mySocket = socket.socket()
mySocket.bind((host, port))

mySocket.listen(1)
conn, addr = mySocket.accept()
print("Connection from: " + str(addr))
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    data = str(data)
    print ("Client: " + str(data))
    msg = input('Server ->')
    conn.send(msg.encode())
            
conn.close()
