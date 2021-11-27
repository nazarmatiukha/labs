import matplotlib.pyplot as plt
from collections import Counter

with open ('text.txt', 'r', encoding='utf-8') as f:
    for i in f:
        text = i
    chars = " !#$%&'()*+,-./:;<=>?@^_`{|}~–«»"
    for x in chars:
        if x in i:
            text = text.replace(x, '')
c = Counter(text)
plt.bar(*zip(*c.most_common()), width=0.5, color='lightblue')
plt.show()