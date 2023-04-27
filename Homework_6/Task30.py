a = int(input("Введите первый элемент "))
n = int(input("Введите разность элементов "))
d = int(input("Введите количество элементов "))

for i in range(d):
    print (a+i*n, end=" ")
