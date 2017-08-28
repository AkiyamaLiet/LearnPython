# -*- coding:utf-8 -*-
"用Python制作计时器"
import time
count = 0 
a = input('time:') 
b = a * 60 
while (count < b):
    ncount = b - count 
    print ncount 
    time.sleep(1)
    count += 1 
print 'done' 