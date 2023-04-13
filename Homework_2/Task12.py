print("Задумайте два натуральных числа от 1 до 1000")
summ = int(input("Введите сумму этих чисел: "))
mult = int(input("Введите произведение этих чисел: "))
first_num = 0
second_num = 0
for i in range(1, 1000):
    for n in range(1, 1000):
        if i+n == summ and i*n == mult:
            first_num = i
            second_num = n

if first_num==0 and second_num==0:
    print ("Обманывать нехорошо!")
else:
    print(f"Первое число {first_num}, второе число {second_num}")
