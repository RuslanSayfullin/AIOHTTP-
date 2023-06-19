sentence = "The quick brown fox jumps over the lazy dog"
letter_count = {}   # Создаем пустой словарь

for letter in sentence:
    if letter.isalpha():    # если символ буква
        if letter.lower() in letter_count:
            letter_count[letter.lower()] += 1   # увелечение счетчик
        else:
            letter_count[letter.lower()] = 1    # первое вхождение-создаем ключ

print(letter_count)

