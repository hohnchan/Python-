#题目012：判断101-200之间有多少个素数，并输出所有素数#
num=[]
for a in range (101,200):
    for b in range(2,a-1):
        if a%b == 0:
            break
    else:
        num.append(a)
print(len(num))
print(num)
