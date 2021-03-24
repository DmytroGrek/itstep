# Напишіть програму word_counter.py, яка приймає як аргумент назву файлу,
# та роздруковує кількість слів в файлі.
with open('file_with_word.txt', 'r') as f:
    num_words = 0
    for words in f:
        num_words += len(words.split())
    print(num_words)
