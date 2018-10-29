windows_size = 3
packet_lost = 5

data = [1,2,3,4,5,6,7,8,9,10]

print "Packets = "
print data

pointer = 0
count = 0

def send(pointer,flag):
    if flag==0:
        print data[pointer:pointer+windows_size]
    elif flag==1:
        print data[pointer]

while(pointer<len(data)):
    #print pointer
    #print count
    if(count >= packet_lost):
        print "packet lost"
        count = 1
        pointer -= 1
        send(pointer,1)
        pointer += 1
    else:
        send(pointer,0)
        pointer += 1
        count += 1
    


