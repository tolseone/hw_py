def Fibonachi(n):
    if n in [1,2]:
        return 1
    return Fibonachi(n - 1) + Fibonachi(n - 2)



list_1 = []
for i in range(1, 8):
    list_1.append(Fibonachi(i))
print(list_1)