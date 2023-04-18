import random

my_list = [random.randint(0, 10) for n in range(
    int(input("Ввведите кол-во элементов списка: ")))]
print(my_list)
k = int(input("Введите элемент: "))
if k in my_list:
    print(f"Элемент {k} есть в списке.")
else:
    min_different = abs(k-my_list[0]) # берем минимальную разницу по первому элементу списка
    nearest_value = my_list[0] # ближаййшее значение по первому элементу
    for n in my_list:
        if abs(n-k)<min_different:
            min_different = abs(n-k)
            nearest_value = n
    print (nearest_value)
