from collections import defaultdict
import pickle
with open ('dopwords.pickle', 'rb') as f:
    words = pickle.load(f)
class Dictionary():
    def __init__(self, rusword, engword, addeng, addrus):
        self.rusword = rusword
        self.engword = engword
        self.addeng = addeng
        self.addrus = addrus


    def eng_search(self):
        result = defaultdict(list)
        for k, vs in words.items():
            for v in vs:
                result[v].append(k)
        engwords = ', '.join(result.get(self.rusword))
        return engwords


    def rus_search(self):
        ruswords = ', '.join(words.get(self.engword))
        return ruswords


    def add(self):
        for i in range (1):
            words.setdefault(self.addeng, []).append(self.addrus)
            with open ('dopwords.pickle', 'wb') as f:
                pickle.dump(words, f)
            with open('dopwords.pickle', 'rb') as f:
                data = pickle.load(f)
                return self.addeng
while True:
    print ("Приветствую в словаре!")
    choice=input('Выберите действие: 1. Поиск русского слова, 2. Поиск английского слова, 3. Добавить слова в словарь, 4. Вывести словарь ' '')
    if choice == '1':
        rusword = input ('Введите слово на русском: ' '')
        d = Dictionary(rusword, 0, 0, 0)

        try: print("Найденное английское слово:",d.eng_search())
        except TypeError:
            print ('Слово не найдено')

    elif choice == '2':
        engword = input ('Введите слово на английском: ' '')
        d = Dictionary(0, engword, 0, 0)

        try: print("Найденное русское слово:", d.rus_search())
        except TypeError:
            print ('Слово не найдено')
    elif choice == '3':
        addeng = input ('Введите слово на английском для добавления в словарь ' '')
        addrus = input ('Введите слово на русском для добавления в словарь ' '')
        d = Dictionary(0, 0, addeng, addrus)
        print ('Слово', d.add(), 'было добавлено')
    elif choice == '4':
        print (words)
    else:
        print('Выберите валидное действие')
