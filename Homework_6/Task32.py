import random

my_list = [random.randint(0,10) for n in range(int(input("Ввведите кол-во элементов списка 1: ")))]
print (my_list)
min_ = int (input("Введите min "))
max_ = int (input("Введите max "))
for n in range (len(my_list)):
    if max_>my_list[n]>min_:
        print (n, end=" ")