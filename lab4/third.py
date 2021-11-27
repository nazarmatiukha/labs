word_list = open('text.txt').read().split()
text = open('text.txt').read()
stopwords = open('stopword.txt').read()
filtered_word_list = word_list[:]#make a copy of the word_list
for word in word_list: # iterate over word_list
  if word in stopwords: 
    filtered_word_list.remove(word)

print ("Текст:\n", text)
print ("\nТекст без стоп слов:\n", *map(str, filtered_word_list))
print ("\nКоличество слов в тексте без стоп-слов:", len(filtered_word_list))
print ("Общее количество слов в тексте:", len(word_list))
print ("Процент воды", len(word_list)/len(filtered_word_list))