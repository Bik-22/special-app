N = int(input("Введите число: "))
for i in range(N, 0, -1):
    row = ""
    for j in range(N, 0, -1):
        if j > i:
            row += str(j)
        else:
            row += "."
    for k in range(1, N + 1):
        if k > i:
            row += str(k)
        else:
            row += "."
    print(row)




