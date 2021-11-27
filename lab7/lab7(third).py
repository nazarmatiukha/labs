import matplotlib.pyplot as plt
import re
from collections import Counter

with open('text.txt', 'r', encoding = 'utf-8') as f:
    for i in f:
        text = i
        chars = re.compile(r"\.\.\.|\.|\!|\?")
        c = Counter(chars.findall(text))
plt.bar(*zip(*c.most_common()), width=0.5, color='lightblue')
plt.show()
