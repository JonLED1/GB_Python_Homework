a = input ("Введите 3-х значное число: ")
if len(a)!=3:
    print ("Обманывать не хорошо!!!")
    exit()
summ = int(a[0]) + int(a[1]) + int(a[2])
print (f"Сумма цифр числа {a} равна {summ}")