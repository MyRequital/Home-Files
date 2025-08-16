def find_longest_word_length(text):
  """Находит длину самого длинного слова в тексте.

  Args:
    text: Строка, содержащая текст.

  Returns:
    Длина самого длинного слова в тексте.
  """
  words = text.split()
  max_length = 0
  for word in words:
    max_length = max(max_length, len(word))
  return max_length

# Пример использования
text1 = "Меня зовут Пётр"
length1 = find_longest_word_length(text1)
print("Длина самого длинного слова:", length1)

text2 = "Меня зовут Василий"
length2 = find_longest_word_length(text2)
print("Длина самого длинного слова:", length2)