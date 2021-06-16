'''
Title     : Python If-Else
Subdomain : Introduction
Domain    : Python
Author    : Utkarsh Mishra
Created   : 27 Jan 2021
Problem   : https://www.hackerrank.com/challenges/py-if-else/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
  N = int(input().strip())
if(N%2!=0):
    print("Weird")
else:
    if(N>=2 and N<=5):
        print("Not Weird")
    elif(N>=6 and N<=20):
        print("Weird")
    else:
        print("Not Weird")
        
