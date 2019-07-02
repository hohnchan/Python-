#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制
a=int(input('请输入一个0到9之间的数字a：'))
num=0
for i in range(0,6):
    num+=a*i*(10**(5-i))
print('数字s=a+aa+aaa+aaaa+aaaaa的计算结果为：',num)