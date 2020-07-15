#2) Дан список целых чисел. Подсчитать сколько четных чисел в списке
x = int(input('Введите 0 или 1:\n'))
a = list(input('Введите элементы списка:\n').split())
s = 0
i = 0
l = len(a)
if x == 0:
    while i < l:
        if int(a[i]) % 2 == 0:
            s += 1
        i += 1
    print(f'{s}, с использованием цикла while')
elif x == 1:
    for i in range(len(a)):
        if int(a[i]) % 2 == 0:
            s += 1
    print(f'{s}, с использованием цикла for')