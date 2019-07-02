num = int(input('请输入一个不大于100的整数：'))
yinshu=[]
for i in range (2,num):
    while True:
        if num%i == 0: #当输入的整数能被i整除
            yinshu.append(i) #将i添加到列表yinshu
            num = num/i#输入的整数等于num/i ,重新进入循环
        else:
            break#结束循环
print(yinshu)



#第一轮，从2，3，4，5开始除，直到出现一个不能整除的数字，num变成最后一轮被整除后的余数
#进行第二轮，再次从整除
#如果不适用wile 循环，第一轮出现不能整出的数字之后即结束