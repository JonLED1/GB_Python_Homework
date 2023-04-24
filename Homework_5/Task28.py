a = int(input ("Введите число А: "))
b = int(input ("Введите число B: "))

def summ(a,b):
    if b==0:
        return a
    return summ(a+1,b-1)
    
print (summ(a,b))