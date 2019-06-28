arr = []
for x in range(1,5):
    for y in range (1,5):
        for z in range (1,5):
            number = [100 * x + 10 * y + z]
            if x!=y and y!=z and z!=x and number not in arr:#互不相同且无重复数字的三位数
                arr.append(number)#添加改数字重复循环
print(len(arr),arr)
