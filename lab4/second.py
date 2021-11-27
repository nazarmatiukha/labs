words = 0
chars = 0
num_chars = 0
uniques = set()
for line in open('test.txt', encoding = 'utf-8'):
    chars += len(line)
    word_list = ' '.join(line.splitlines()).split()
    for x in word_list:
        num_chars += len(x)
    pos = 'out'
    for char in line:
        if char != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif char == ' ':
            pos = 'out'
    uniques |= set(line.split())
print("Общее количество символов:", chars)
print ("Количество символов без пробелов:", num_chars)
print("Количество слов:", words)
print ("Количество уникальных слов:", len(uniques))