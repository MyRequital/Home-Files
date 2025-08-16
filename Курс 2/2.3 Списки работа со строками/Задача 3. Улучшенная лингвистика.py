"""
Мы уже писали программу для лингвистов, которая считала количество определённых букв в тексте.
Теперь эту программу нужно улучшить. Есть список из трёх слов, которые вводит пользователь.
Затем вводится сам текст произведения строго по словам. Текст вводится до тех пор, пока не встретится слово end.
Напишите программу, которая посчитает, сколько раз слова пользователя встречаются в тексте.
"""
text = []
while True:
    text_input = input("Введите текст: ")
    if text_input == "end":
        break
    else:
        text.append(text_input)

trigger_list = []
trigger_list_search = []
trigger_count = 0

for i in range(3):
    selected_words_input = input(f"Введите {i + 1} слово: ")
    trigger_list.append(selected_words_input)

for trigger_word in trigger_list:
    for text_word in text:
        if trigger_word == text_word:
            trigger_count += 1
    trigger_list_search.append([trigger_word, trigger_count])
    trigger_count = 0

for i in trigger_list_search:
    print(i, end=" ")


# text = "я люблю собак потому что они милые когда спят я собак я собак".split(" ")
# print(text)
# trigger_word_1 = "Собак".lower()
# trigger_word_2 = "я".lower()
# print(text.count(trigger_word_1), text.count(trigger_word_2))