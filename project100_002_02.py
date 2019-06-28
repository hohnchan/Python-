net_profit=int(input('净利润:'))
standard = [1000000, 600000, 400000, 200000, 100000, 0]
rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
bonus = 0
for i in range(len(standard)):
    if net_profit > standard[i]:
        bonus+= (net_profit - standard[i])*rate[i]
        net_profit = standard[i]
print(bonus)
