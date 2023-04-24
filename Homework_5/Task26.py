a = int(input ("Введите число А: "))
b = int(input ("Введите число B: "))

def degree(a,b):
    if b==1:
        return a
    return a*degree(a,b-1)
    
print (degree(a,b))