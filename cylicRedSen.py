def partXOR(a,b):
  ans = []
  for i in range(len(b)):
    aa,bb = int(a[i]),int(b[i])
    ans.append( aa^bb )
  return ans

msg = input()
msg = [int(a) for a in msg]
div = [1,0,1,0]
zero = [0,0,0]
msg += zero
zero.append(0)
pack = msg[0:4]
for i in range(len(msg)-1):
  sentDiv = div
  if pack[0] < div[0]:
    sentDiv = zero
  ans = partXOR(pack , sentDiv)
  if (i+3 >= len(msg)):
    break
  ans.pop(0)
  ans.append(msg[i+3])
  pack = ans
ans.pop(0)
print("Checker " , div)
print("Message " , msg)
print("Remainder " , ans)


"""
10110
Checker  [1, 0, 1, 0]
Message  [1, 0, 1, 1, 0, 0, 0, 0]
Remainder  [1, 1, 0]
"""
