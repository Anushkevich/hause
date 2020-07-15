#1) Дан список целых чисел.
#Создать новый список, каждый элемент которого равен исходному элементу
#умноженному на -2
z=input('Введите 0 или 1:\n')
print(z)
a = list(input('Введите целые числа:\n').split())
b = []
print(a)
c = len(a)
i = 0
if int(z) == 0:
 for i in range(c):
  a[i] = int(a[i]) * -2
  b.append(a[i])
 print(f'{b}, с использованием цикла for')
elif int(z) == 1:
 while (i < c):
  a[i] = int(a[i]) * -2
  b.append(a[i])
  i += 1
 print(f'{b}, с использованием цикла while')


