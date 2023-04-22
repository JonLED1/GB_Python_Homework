import random

my_list_1 = [random.randint(0,10) for n in range(int(input("Ввведите кол-во элементов списка 1: ")))]
print (my_list_1)
my_list_2 = [random.randint(0,10) for n in range(int(input("Ввведите кол-во элементов списка 2: ")))]
print (my_list_2)
my_list_3=[]
my_list_1 = set(my_list_1)
my_list_2=set(my_list_2)

for n in my_list_1:
    for i in my_list_2:
        if n==i:
            my_list_3.append(n)
print(my_list_3)

