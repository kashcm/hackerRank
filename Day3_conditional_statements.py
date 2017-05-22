#!/bin/python3

import sys


N = int(input().strip())
if N%2 ==1:
    print('Weird')

if N%2 ==0:
    if N in range(0,5):
        print('Not Weird')
    elif N in range(5,21):
        print ('Weird')
    else:
        print('Not Weird')

