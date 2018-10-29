def redBit(m):
	r = 0
	while ( 2**r - r <= m + 1 ):
		r += 1
	return r

def getBits(data):
	arr = []
	for d in data:
		arr.append(int(d))
	return arr

par = {}
par[1] = [1,3,5,7,9,11]
par[2] = [2,3,6,7,10,11]
par[3] = [4,5,6,7,12,13,14,15,20,21,22,23]
par[4] = [8,9,10,11,13,12,13,14,15]

def devPar(r , data):
	l = len(data) + r
	data2 = []
	j = 0
	data2.append("start")
	for i in range(1,l+1):
		if i in [1,2,4,8,16]:
			data2.append(-1)
		else:
			data2.append(data[j])
			j += 1
			
	for i in range(1,r+1):
		c = 0
		myli = []
		for p in par[i]:
			if p > l:
				break
			elif data2[p] == 1:
				c += 1
			myli.append(data2[p])
			
		print(myli)
		if c%2 == 0:
			data2[2**(i-1)] = 0
		else:
			data2[2**(i-1)] = 1
	
	return data2
	

data = input()
m = len(data)
data = getBits(data)
r = redBit(m)
ans = devPar(r , data)

print( ans )



