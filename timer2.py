#coding:gbk
import time  
import sys
import winsound

def clock():
    now_time = time.ctime()
    print "���ڵ�ʱ����",now_time
    hour_set=int(input("����������Ҫ�������ӵ�Сʱ��"))
    minute_set=int(input("�������������ӵķ��ӣ� "))
    i = 3
    o = 4 
    while i:
        local_time= list(time.localtime())  #��ȡ����ʱ��
        hour_now = local_time[3]  
        minute_now = local_time[4]  
        if hour_now == hour_set and minute_now == minute_set: # ����ʾ����Ľ����ж�  
            i = 0
        time.sleep(60)
    while o:
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS) 
        winsound.PlaySound("*", winsound.SND_ALIAS)
        o -= 1
    print '����'

if __name__ == '__main__':
    clock()
