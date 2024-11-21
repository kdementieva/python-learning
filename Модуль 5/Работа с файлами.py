import re

def get_words(filename):
  words =[]
  with open(filename, 'r', encoding='utf-8') as f:
    for line in f:
      line = re.sub(r'[^\w\s]', '', line) 
      words_in_text = line.lower().strip().split()
      words.extend(words_in_text)
  return words

def get_words_dict(words):
  words_dict = {}
  for word in words:
    words_dict[word] = words_dict.get(word, 0) + 1
  return words_dict
  
def print_dict(words_dict):
  return '\n'.join(f'{key}: {value}' for key, value in words_dict.items())


filename = input('Введите название файла: ')
words = get_words(filename)
print(f'Кол-во слов: {len(words)}')
words_dict = get_words_dict(words)
print(f'Кол-во уникальных слов: {len(words_dict)}')
words_dict = print_dict(words_dict)
print('Все использованные слова:')
print(words_dict)