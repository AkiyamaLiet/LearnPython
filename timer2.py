#coding:gbk
import time  
import sys
import winsound

def clock():
    now_time = time.ctime()
    print "现在的时间是",now_time
    hour_set=int(input("请输入您想要设置闹钟的小时："))
    minute_set=int(input("请输入设置闹钟的分钟： "))
    i = 3
    o = 4 
    while i:
        local_time= list(time.localtime())  #获取本地时间
        hour_now = local_time[3]  
        minute_now = local_time[4]  
        if hour_now == hour_set and minute_now == minute_set: # 把提示输入的进行判断  
            i = 0
        time.sleep(60)
    while o:
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS) 
        winsound.PlaySound("*", winsound.SND_ALIAS)
        o -= 1
    print '结束'

if __name__ == '__main__':
    clock()
