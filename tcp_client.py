import socket
 
host = '127.0.0.1'
port = 5001
        
mySocket = socket.socket()
mySocket.connect((host,port))
        
message = input("Client -> ")
        
while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()
                
        print ('Server: ' + data)
                
        message = input("Client -> ")
                
mySocket.close()
