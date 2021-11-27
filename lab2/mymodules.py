from random import randint
from functools import reduce
"""На выбор 2 типа списка ради удобства, в return переводим значение в list""" 
def opt():
    print (">>>Приветствую! Выберите, с каким списком хотите работать: 1. Произвольный список, 2. Случайный список")
    option = str (input ())
    if option == '1':
        e=int(input("Введите размер списка: "))
        print ("Введите элементы списка: ")
        A = []
        for i in range (e):
            A.append(int(input()))
        return list(A)
    elif option == '2':
        A = []
        for h in range(10):
            A.append(randint(-100, 100))
        return list(A)
    else:
        print ("Выберите валидный список")
"""Выводим функцию в переменную для сохранения элементов введённых вручную или из randint"""
spisok = opt()
"""Просто сортируем список с помощью функции sorted, присваиваем значение из return переменной"""
def sortd():
    return sorted(spisok)
sortdlist = sortd()
"""Доп. функция ради удобства, действия те же"""
def sortdrev():
    srev = spisok
    return list(sorted(srev, reverse = True))
sortdrev = sortdrev()
"""Вводим число через инпут, сохраняем, проверяем и обрабатываем через index. Т.к. индексация начинается с 0,
 стартуем с +1"""
def search():
    search = int (input ("Введите значение для поиска: "))
    s_check = search in spisok
    if s_check == True:
        print (" ", "Элемент есть в списке")
        print (" ", "Номер элемента в первоначальном списке:", spisok.index (search)+1)
        print (" ", "Номер элемента в отсортированном списке:", sortdlist.index (search)+1)
    else:
        print (" ", "Элемента нет в списке")

"""Временно переводим обыч. и сорт. списки в стринг, чтобы можно было ввести нужные значения через 
запятую и это было легче оформить"""
def sequence():
    elseq = str(input("Введите последовательность элементов (через запятую и пробел): "))
    listspis = str(spisok)
    listspisrev = str(sortdlist)
    if elseq in listspis:
        print (" ", "Последовательность", elseq, "найдена в изначальном списке")
    elif elseq in listspisrev:
        print ("Последовательность ", elseq," не найдена в изначальном списке, но найдена в сортированном списке")
    else:
        print (" ", "Последовательность не найдена")
"""Тут через цикл прогоняем от 0 до 5 все числа из сортированного списка, берём обыч. сорт. список для 5 мин. элементов,
 т.к. они там уже по госту рассортированы, аналогично с перевёрнутым"""
def fiveminel():
    for i in range (0, 5):
        print (sortdlist[i])
def fivemaxel ():
    for x in range (0, 5):
        print (sortdrev[x])
"""Простая формула, переводим в float для точного отображения"""
def arith_mean():
        return float (sum(spisok)) / max(len(spisok), 1)
"""Задаём пустой список, цикл пробегается по изначальному списку, если элементов из списка нет в doplist, то
 он наполняет его этими элементами"""
def unique():
        doplist = []
        for a in spisok:
            if a not in doplist:
                doplist.append(a)
                yield a

"""Ищем наибольшее общее кратное"""
def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a
"""Ищем наименьшее общее кратное"""
def lcm(a, b):
    return a * b // gcd(a, b)
"""Даём значения для операции, выводим"""
def lcmm(spisok):
    return reduce(lcm, spisok)
"""Создаём пустой список, цикл прогоняет изнач. список и на каждый элемент цепляет счётчик"""
def duplicate():
    dupl = {}
    for i in set(spisok):
        dupl[i] = spisok.count(i)
    return dupl
def shift():
    shift = int(input("Введите на сколько элементов нужно сместить список: "))
    lst = spisok[-shift:] + spisok[:-shift]
    return lst