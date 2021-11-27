import math


class Format:
    end = '\033[0m'
    underline = '\033[4m'


class Library():
    def __init__(self, booknum, bookdel, name, author, year, genre, searching):
        self.booknum = booknum
        self.bookdel = bookdel
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.searching = searching
        self.path = open('data.txt', encoding = 'utf-8').read()

    def booknum_check(self):
        with open('data.txt', encoding = 'utf-8') as f:
            for line in f:
                if self.booknum in line:
                    return 1

    def bookdelete_check(self):
        with open('data.txt', encoding = 'utf-8') as f:
            for line in f:
                if self.bookdel in line:
                    return 1

    def name_add(self):
        with open('data.txt', 'a', encoding='utf-8') as f:
            f.write(" "+self.name+" "+'[1]'+self.booknum)

    def author_add(self):
        with open('data.txt', 'a', encoding='utf-8') as f:
            f.write(" "+self.author+" "+'[2]'+self.booknum)

    def year_add(self):
        with open('data.txt', 'a', encoding='utf-8') as f:
            f.write(" "+self.year+" "+'[3]'+self.booknum)

    def genre_add(self):
        with open('data.txt', 'a', encoding='utf-8') as f:
            f.write(" "+self.genre+" "+'[4]'+self.booknum)

    def view(self):
        with open('data.txt', encoding='utf-8') as f:
            for line in f:
                string = line.split()
                d = [string[3*i:3*i+3] for i in range(0,math.ceil(len(string)/3))]
                for i in d:
                    if i[1] == '[1]':
                        n = i[0]
                        yield '\n'+n.replace("_", " ")

    def bookdelete(self):
        with open("data.txt", "r", encoding='utf-8') as f:
            for lined in f:
                lines = lined.split()
                d = [lines[3 * i:3 * i + 3] for i in range(0, math.ceil(len(lines) / 3))]
                for i in d:
                    if self.bookdel in i[0].replace("_", " "):
                        numconst = i[2]
                for m in d:
                    if numconst in m and m[1] == '[1]':
                        book_n = m[0]
                        d.remove(m)
                for x in d:
                    if numconst in x and x[1] == '[2]':
                        d.remove(x)
                for p in d:
                    if numconst in p and p[1] == '[3]':
                        d.remove(p)
                for e in d:
                    if numconst in e and e[1] == '[4]':
                        d.remove(e)
            with open("data.txt", "w", encoding='utf-8') as f:
                for on in d:
                    f.write(on[0] + ' ' + on[1] + ' ' + on[2] + ' ')
                return "Книга "+ Format.underline + book_n.replace("_", " ")+ Format.end + " удалена"

    def search(self):
        with open('data.txt', encoding='utf-8') as f:
            for line in f:
                string = line.split()
                d = [string[3*i:3*i+3] for i in range(0,math.ceil(len(string)/3))]
                for i in d:
                    if self.searching in i[0].replace("_", " "):
                        numconst = i[2]
                for m in d:
                    if numconst in m and m[1] == '[1]':
                        book_n = m[0]
                    if numconst in m and m[1] == '[2]':
                        book_auth = m[0]
                    if numconst in m and m[1] == '[3]':
                        book_y = m[0]
                    if numconst in m and m[1] == '[4]':
                        book_g = m[0]
                        return 'Вероятнее всего, вы имели ввиду книгу ' + Format.underline + \
                               book_n.replace("_", " ") + Format.end + '\nОстальные найденные данные:' + '\n  Автор: ' \
                               + book_auth.replace("_", " ") + \
                               '\n  Год выпуска: ' + book_y.replace("_", " ") + '\n  Жанр: ' + book_g.replace("_", " ")


while True:
    choice = input("Выберите действие: 1. Просмотр всех книг, 2. Поиск книги, 3. Добавление книги, 4. Удаление книги: ")
    if choice == '1':
        my_lib = Library(0, 0, 0, 0, 0, 0, 0)
        print(*my_lib.view())
    elif choice == '2':
        searchingentry = input("Введите что желаете найти: ")
        my_lib = Library(0, 0, 0, 0, 0, 0, searchingentry)
        try: my_lib.search()
        except UnboundLocalError:
            print("Книга не найдена")
            continue
        print(my_lib.search())
    elif choice == '3':
        booknumentry = " num" + input("Укажите номер книги: ")
        my_lib = Library(booknumentry, 0, 0, 0, 0, 0, 0)
        if my_lib.booknum_check() == 1:
            print("Номер уже занят")
        else:
            names = (input("Введите название книги: ").replace(" ", "_"))
            authors = (input("Введите автора книги: ").replace(" ", "_"))
            years = (input("Введите год выпуска книги: ").replace(" ", "_"))
            genres = (input("Введите жанр книги: ").replace(" ", "_"))
            my_lib = Library(booknumentry, 0, names, authors, years, genres, 0)
            my_lib.booknum_check()
            my_lib.name_add()
            my_lib.author_add()
            my_lib.year_add()
            my_lib.genre_add()
    elif choice == '4':
        my_lib = Library(0, 0, 0, 0, 0, 0, 0)
        print("Список книг:")
        print(*my_lib.view())
        print("Выберите книгу из предложенных для удаления(введите название, автора, год или жанр):")
        bookdel = input()
        my_lib2 = Library(0, bookdel, 0, 0, 0, 0, 0)
        if my_lib2.bookdelete_check() == 1:
            print(my_lib2.bookdelete())
        else:
            print ("Введите название книги")

    else:
        print("Выберите вариант из предложенных, введите цифру")



