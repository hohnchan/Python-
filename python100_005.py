#题目005：输入三个整数,x,y,z, 请把这三个数有小到大输出#
print("请输入三个整数x,y,z")
x = int(input('x='))
y = int(input('y='))
z = int(input('z='))

a=(x , y , z)
b=sorted(a)
print(b)


