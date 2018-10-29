#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 04:36:22 2018

@author: ncheck
"""
import time
import random

t = 5
prev = -1
window = 3
ans = []
while t > 0:
    t -= 1
    if prev == window - 1:
        prev = -1
    time.sleep(0.5)
    i = -1
    while i < window-1:
        i += 1       
        time.sleep(0.25)
        send = i
        print("Sending " , send  ,end = " ")
        err = random.randint(0,window)
        if err == send:
            print("**ERROR** Sending NAK for " , send)
        else:
            print(" recieved" , send)
            if send != 0 and prev+1 != send:
                print(" Go Back" , send)
                ans.append(-1*send)
                i = prev
            else:
                ans.append(send)
                prev = send

print(ans)


"""
Sending  0  recieved 0
Sending  1  recieved 1
Sending  2  recieved 2
Sending  0  recieved 0
Sending  1  recieved 1
Sending  2  recieved 2
Sending  0 **ERROR** Sending NAK for  0
Sending  1 **ERROR** Sending NAK for  1
Sending  2  recieved 2
 Go Back 2
Sending  0  recieved 0
Sending  1  recieved 1
Sending  2  recieved 2
Sending  0  recieved 0
Sending  1 **ERROR** Sending NAK for  1
Sending  2  recieved 2
 Go Back 2
Sending  1 **ERROR** Sending NAK for  1
Sending  2  recieved 2
 Go Back 2
Sending  1  recieved 1
Sending  2  recieved 2
Sending  0  recieved 0
Sending  1  recieved 1
Sending  2 **ERROR** Sending NAK for  2
[0, 1, 2, 0, 1, 2, -2, 0, 1, 2, 0, -2, -2, 1, 2, 0, 1]
"""