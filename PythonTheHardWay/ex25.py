def break_words(stuff):
  words = stuff.split()
  return words

def sort_words(words):
  return sorted(words)

def print_first_word(words):
  word = words.pop(0)
  print(word)

def print_last_word(words):
  word = words.pop(-1)
  print(word)

def sort_sentance(sentance):
  words = break_words(sentance)
  return sort_words(words)

def print_fist_and_last(sentance):
  words = break_words(sentance)
  print_first_word(words)
  print_last_word(words)

def print_first_word_sorted(sentance):
  words = sort_sentance(sentance)
  print_first_word(words)
  print_last_word(words)
