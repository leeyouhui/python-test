import time
from idlelib.IOBinding import encoding
# 获取当前时间
ISOTIMEFORMAT='%Y-%m-%d %X'
def getCurrentTime():
    cur_time = time.strftime(ISOTIMEFORMAT, time.localtime())
#     print (cur_time);
    return cur_time;
# getCurrentTime()

def str2Bytes(s):
    return bytes(s,encoding = 'utf-8');

def bytes2Str(bs):
    return str(bs,encoding = 'utf-8');