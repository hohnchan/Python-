#暂停一秒返回值，并将时间格式化#
import time
a = time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time()))#time.localtime()，时间戳转换为时间元祖#
print(a)
time.sleep(1)
b =  time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time()))#time.strftime(),时间元祖转换为时间文本#
print(b)


