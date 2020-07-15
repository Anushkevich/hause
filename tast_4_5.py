#5) Составить список чисел Фибоначчи содержащий 15 элементов.
#(Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны
#либо 1 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
#Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )
a=input('Введите 0 или 1:\n')
b = []
i = 0
n = 15
if a == 0:
    while i < n:
        if i == 0:
            b.append(0)
            i += 1
            continue
        elif i == 1:
            b.append(1)
            i += 1
            continue
        else:
            b.append(b[i - 1] + b[i - 2])
            i += 1
    print(b)
if a == 1:
    for i in range(n):
        if i == 0:
            b.append(0)
            continue
        elif i == 1:
            b.append(1)
            continue
        else:
            b.append(b[i - 1] + b[i - 2])
    print(b)