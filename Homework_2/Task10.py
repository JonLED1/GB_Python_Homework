import random

avers = 0
revers = 0
num_coin = int(input("Ведите количество монет: "))
for i in range(num_coin):
    side = random.randint(0, 1)  # 0-avers, 1-revers
    if (side == 0):
        avers += 1
    else:
        revers += 1
    print(side, end=" ")
print()
if avers > revers:
    print(revers)
else:
    print(avers)
