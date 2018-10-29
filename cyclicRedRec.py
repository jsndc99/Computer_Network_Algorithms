def partXOR(a,b):
  ans = []
  for i in range(len(b)):
    aa,bb = int(a[i]),int(b[i])
    ans.append( aa^bb )
  return ans

msg = input()
msg = [int(a) for a in msg]
div = [1,0,1,0]
zero = [0,0,0,0]
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

print("remainder " , ans)

print("Checker " , div)
print("Message " , msg)
print("Error") if 1 in ans else print("No Error")


"""

10110110
remainder  [0, 0, 0]
Checker  [1, 0, 1, 0]
Message  [1, 0, 1, 1, 0, 1, 1, 0]
No Error

"""
