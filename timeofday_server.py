import socket
import time
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

# declare our serverSocket upon which
# we will be listening for UDP messages
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

#Encode Message before Sending
#Decode Message before Recieving
#Python3 ka Rules

while True:
    data, addr = serverSock.recvfrom(1024)
    data = data.decode()
    print ("Client: ", addr[0],  addr[1])
    myT = time.localtime()
    Time = str(myT.tm_hour) + " hrs " + str(myT.tm_min) + " min " + str(myT.tm_sec) + " sec"
    Date = str(myT.tm_mday) + '/' + str(myT.tm_mon) + '/' + str(myT.tm_year)
    Reply = "Date -> " + Date + " Time ->" + Time
    Reply = Reply.encode()
    serverSock.sendto(Reply, (addr[0], addr[1]))
    #Addr 0 has client IP, and Addr 1 has client port