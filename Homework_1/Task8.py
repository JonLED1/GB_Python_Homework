n = int(input("Долек по горизонтали:"))
m = int(input("Долек по вертикали:"))
k = int(input("Долек отломить:"))
if k < m*n and (k % n == 0 or (k % m == 0)):
    print("YES")
else:
    print("NO")
