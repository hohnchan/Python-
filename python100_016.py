#输出指定格式的日期,可用time包完成
import time
print(time.time()) #时间戳
print(time.localtime())#时间元组
print(time.asctime())#时间的一种可读文本形式
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))#按指定文本格式输出时间

st = time.localtime(time.time())#时间戳转化为时间元组
st = time.strptime('2019/6/28','%Y/%m/%d')#时间文本转化为时间元组
date = time.strftime('%Y-%m-%d',st)#时间元组转化为时间文本
print(date)#将时间文本格式化
