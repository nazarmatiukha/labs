from mymodules import spisok, sortd, sortdlist, search, sequence, fiveminel, fivemaxel, arith_mean, unique, lcmm, duplicate, shift, opt
print ("Изначальный список", spisok)
print("Сортированный список", sortdlist)
search()
sequence()
print("Первые пять минимальных элементов:"), fiveminel()
print("Первые пять максимальных элементов:"), fivemaxel()
print("Среднее арифметическое:", arith_mean())
print("Список без повторных элементов:", [*unique()])
print("Наименьшее общее кратное:", lcmm(spisok))
print("Повторения элементов:", duplicate())
print("Список с циклическим сдвигом: ", shift())