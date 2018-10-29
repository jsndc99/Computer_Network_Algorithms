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
	j = 0
	data = data[::-1]
	data.append("start")
	data = data[::-1]
	ans = "NO ERROR"
	l = len(data)
	myli = []			
	for i in range(1,5):
		c = 0
		for p in par[i]:
			if p > l-1:
				break
			elif data[p] == 1:
				c += 1
		if c%2 != 0:
			ans = "ERROR DETECTED at bit "
			myli.append(i)
	error = 0
	if len(myli) == 0:
		return ans
	for i in myli:
		error += 2**(i-1)
	return ans + str(error)
	

data = input()
m = len(data)
data = getBits(data)
r = redBit(m)
ans = devPar(r , data)

print( ans )

"""

11101010101
NO ERROR

11101010111
ERROR DETECTED at bit 10
"""
