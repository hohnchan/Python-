#有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子。假如兔子都不死。问每个月的兔子总数为多少？#

num = int(input('请输入月份：'))
tuzi=[1,1]
for i in range(0,num-2):
    tuzi.append(tuzi[-1]+tuzi[-2])
print('%d月后有兔子%d对'%(num,tuzi[-1]))