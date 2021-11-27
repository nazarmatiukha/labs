import math
N = []
e=int(input("Введіть розмір масиву: "))
print ("Введіть елементи масиву: ")
for c in range (e):
    N.append(int(input()))
print ("Масив: ")
print (N)
max_neg_abs = max((i for i in N))
if max_neg_abs < 0:
    print ("Максимальний від'ємний елемент:", max_neg_abs)
else:
    print ("Від'ємні елементи відсутні")
multiply = 0
print ("Добуток від'ємних чисел:")
def mult(d):
    oper = 1
    for i in d:
        if i<0:
            oper *= i
    return oper
print (mult(N))
print ("Ненульові елементи у зворотньому порядку:")
for i in reversed(N):
    if i != 0:
        print (i, end = ', ')