#题目004：输入某年某月某日，判断这一天是这一年的第几天#
import time
date = input('请输入时间（例如2019-04-11）:')
st = time.strptime(date,'%Y-%m-%d')#时间文本转换为时间元祖#
num = st.tm_yday
print(num)
