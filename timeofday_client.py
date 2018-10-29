import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#Encode Message before Sending
#Decode Message before Recieving
#Python3 ka Rules


Message = "Time of Day"

Message = Message.encode()
clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))

Reply,addr = clientSock.recvfrom(1024)

print('Server: ', Reply.decode())

clientSock.close()