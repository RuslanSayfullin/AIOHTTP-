import pymorphy2

# Создаем экземпляр обьекта MorphAnalyzer
morph = pymorphy2.MorphAnalyzer()

# анализируем слово и выводим его форму в родительном падеже единственного числа
work = "котик"
parsed_word = morph.parse(word)[0]
print(parser-word.inflect({'gent'}).word)   # выводим 'котка'
