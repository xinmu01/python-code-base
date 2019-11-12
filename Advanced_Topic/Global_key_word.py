# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 23:46:05 2019

@author: Xin
"""

##Global keyword

accum = 0

for i in range(1,6):
    accum += i

print ("accum is {}".format(accum))

def test_global():
    global accum
    for i in range(1,6):
        accum += i
    print ("accum is {}".format(accum))
    
test_global()