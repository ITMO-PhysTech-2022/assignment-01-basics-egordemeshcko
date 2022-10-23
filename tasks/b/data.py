"""
Вам дана переменная n, в которую записано целое число.

Создайте массив a длины n, в котором каждое следующее число так же
генерируется функцией get_integer().

Выведите по очереди:
- сам массив
    > уже написано за вас
- [a] первый, медианный (центральный) и последний элемент массива через пробел
    > если длина массива четная, то центральным считайте первый из двух центральных
- [b] минимальный и максимальный элементы массива через пробел
- [c] сумму всех элементов массива
- [d] массив, состоящий из квадратов всех четных элементов a
- [e] позицию первого вхождения минимального элемента в a
- [f] развернутый массив a
    > подсказка: используйте встроенную функцию или срез
- [g] массив, состоящий из всех элементов a на четных позициях
    > подсказка: используйте срез
"""

from test.common.context import get_integer

n = get_integer()
a = ...

# Место для вашего кода (заполнение массива)
a=[]
b=[]
v=[]
for i in range(6):
   k = get_integer()
   a.append(k)
   if (k % 2) == 0: b.append(k**2)
   if (i % 2) == 0: v.append(k)
print(a)
# Место для вашего кода
if len(a) % 2 == 1:
   g=a[int(len(a)//2)]
else: g=a[int(len(a)//2)-1]
print(a[0], g, a[-1])
print(min(a),max(a))
print(sum(a))
print(b)
print(a.index(min(a)))
a.reverse()
print(a)
print(v)