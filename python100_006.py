#斐波那契数列#

a = [0,1]
for i in range(10):
    a.append(a[-1] + a[-2])
print(a)
