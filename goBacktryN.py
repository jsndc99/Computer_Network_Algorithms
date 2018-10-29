windows_size = 3
packet_lost = 5

data = [1,2,3,4,5,6,7,8,9,10]

print "Packets = "
print data

pointer = 0
count = 0

def send(pointer):
    print data[pointer:pointer+windows_size]

while(pointer<len(data)):
    #print pointer
    #print count
    if(count >= packet_lost):
        print "packet lost"
        count = 2
        pointer -= 1
    send(pointer)
    pointer += 1
    count += 1
    


