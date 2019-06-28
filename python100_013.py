#打印出所有的"水仙花数"#
shuixianhua=[]
for a in range(1,9):
    for b in range(0,9):
        for c in range(0,9):
            num = 100*a + 10*b +c
            if num == a**3+ b**3+ c**3:
                shuixianhua.append(num)
            else:
                break
print(shuixianhua)
