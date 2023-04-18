import random

my_list = [random.randint(0,10) for n in range(int(input("Ввведите кол-во элементов списка: ")))]
print (my_list)
print (my_list.count(int(input("Введите элемент: "))))