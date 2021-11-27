from random import randint

cont = 'y'
while cont == 'y':
    print (">>>Приветствую! Выберите, с каким списком хотите работать: 1. Произвольный список, 2. Случайный список, 3. Прошлый список ")
    option = int(input ())
    if option == 1:
        A = []
        e=input("Введите размер списка: ")
        print ("Введите элементы списка: ")
        for i in range (e):
            A.append(int(input()))
    elif option == 2:
        A = []
        for i in range(10):
            A.append(randint(-1, 100))
    else:
        print ("Введите валидные значения")
    try: A
    except NameError:
        print ("Нет списков в буфере, выберите произвольный или случайный список")
        continue
    print ("Список", A)
    sortspisok = sorted(A)
    sortspisokrev = sorted (A, reverse=True)
    print ("Сортированный список:", sortspisok)
    search = int(input ("Введите значение для поиска: "))
    s_check = search in A
    if s_check == True:
        print (" ", "Элемент есть в списке")
        print (" ", "Номер элемента в первоначальном списке:", A.index (search)+1)
        print (" ", "Номер элемента в отсортированном списке:", sortspisok.index (search)+1)
    else:
        print (" ", "Элемента нет в списке")
    
        
    elseq = str(input("Введите последовательность элементов (через запятую): "))
    listspis = str(A)
    listspisrev = str(sortspisok)
    if elseq in listspis:
        print (" ", "Последовательность", elseq, "найдена в изначальном списке")
    elif elseq in listspisrev:
        print ("Последовательность ", elseq," не найдена в изначальном списке, но найдена в сортированном списке")
    else:
        print (" ", "Последовательность не найдена")

    print ("Первые пять минимальных элементов:")
    for i in range (0, 5):
        print (sortspisok[i])
        
    print ("Первые пять максимальных элементов:")
    def sorting ():
        for x in range (0, 5):
            print (sortspisokrev[x])
    sorting()

    def arith_mean():
        return float (sum(A)) / max(len(A), 1)
    print ("Среднее арифметическое:", arith_mean())
    def unique(obj: iter):
        args = []
        a = []
        for a in obj:
            if a not in args:
                args.append(a)
                yield a
    r = unique(A)
    print ("Список без повторных элементов:", [*r])
