profit = int(input("请输入净利润："))

if profit < 100000:
    commission = profit * 0.1
elif profit > 100000 and profit <= 200000:
    commission = 10000 + (profit - 100000) * 0.075
elif profit > 200000 and profit <= 400000:
    commission = 10000 + 7500 + (profit - 200000) * 0.05
elif profit > 400000 and profit <= 600000:
    commission = 22500 + (profit - 400000) * 0.03
elif profit > 600000 and profit <= 1000000:
    commission = 28500 + (profit - 600000) * 0.015
else:
    commission = 39500 + (profit - 1000000) * 0.01
print(commission)