import random
random_words = open('randwords.txt').read().split()
for i in range (random.randint(1, 10)):
    print (random.choice(random_words), end=' ')
