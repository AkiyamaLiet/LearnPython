# -*- coding:utf-8 -*-
"用Python制作计时器"
import time

def Count():
    count = 0 
    min_input = input('time:') 
    sec = min_input * 60 
    while (count < sec):
        sec_now = sec - count 
        #    print sec_now 
        #   输出提示
        min_clk = sec_now / 60
        sec_clk = sec_now % 60
        print "%d:%d" %(min_clk, sec_clk)
        time.sleep(1)
        count += 1 
    print 'done' 
    
if __name__ == '__main__':
    Count()