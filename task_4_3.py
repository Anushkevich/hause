#3) Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
#Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
#‘value’}). Чтобы получить список ключей - использовать метод .keys()
#(подсказка: создается новый ключ с цифрой в конце, старый удаляется)
a= {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
b = list(a.keys())
j = len(a)
for i in list(a.keys()):
  print(f' {i} : {a[i]} -> {i} {len(i)}:  {a[i]}')
  i = 0
while i < j:
   key = b[i]
   a[key + str(len(key))] = a[key]
   a.pop(key)
   i += 1
   print(a)

