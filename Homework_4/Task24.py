n = int(input())  # количество кустов
a = list(map(int, input().split()))  # урожайность каждого куста
max_berries = 0  # максимальное число ягод
for i in range(n):
    berries = a[i] + a[(i+1)%n] + a[(i-1)%n]  # число ягод собранных с куста и его соседей
    max_berries = max(max_berries, berries)  # обновление максимального числа ягод
print(max_berries)  # вывод максимального числа ягод, которое может собрать собирающий модуль