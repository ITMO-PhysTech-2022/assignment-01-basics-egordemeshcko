"""
Считайте с клавиатуры две строки.

Выведите по очереди:
- [a] произведение длин этих строк
- [b] обе эти строки, разделенные пробелом
- [c] обе эти строки, разделенные запятой и табуляцией
- [d] строку вида "Hello, {первая строка}! Just wanted to say: '{вторая строка}'"
    > подсказка: используйте форматную строку (f-string)
- [e] первые "слова" из каждой строки через пробел
    > под "словами" имеются в виду части строки, разделенные друг от друга пробелами
- [f] количество "слов" в первой строке
- [g] первую позицию вхождения первой строки во вторую (или -1, если их нет)
"""

s1 = ...
s2 = ...

# Место для вашего кода
s1=input()
s2=input()
print(len(s1)*len(s2))
print(s1, s2)
print(s1+',',s2)
print('Hello,',s1+'! Just wanted to say: '"'"+s2+"'")
if ' ' in s1 and ' ' in s2:
    print(s1[:s1.index(' ')],s2[:s2.index(' ')])
else:
    if' ' in s1:
        print(s1[:s1.index(' ')],s2)
    else:
        if ' ' in s2:
            print(s1,s2[:s2.index(' ')])
        else:
            print(s1,s2)
h=1
for i in range(len(s1)):
    if s1[i-1] == ' ': h=1+h
print(h)
for n in range(len(s2)):
    if (s2[(n-1):(n+(len(s1))-1)]) == s1:
        print(n-1)
        k=1
        break
if k != 1: print(-1)
