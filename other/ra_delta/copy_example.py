# Задание:
# что мы увидим в результате и почему?
# Как сделать так, чтобы изменения, вносимые в первый список (first_list), не затрагивали второй (second_list)?
import copy

first_list = [[0, 1, 2], [3, 4, 5]]
second_list = list(first_list)
second_list_new = copy.deepcopy(first_list)
first_list.append([6, 7, 8])
first_list[1][0] = 9

print(first_list)
print(second_list)

# Результат:
# [[0, 1, 2], [9, 4, 5], [6, 7, 8]]
# [[0, 1, 2], [9, 4, 5]]
# Такое поведение связано с ссылочной моделью данных в Python, обьекты списков first_list, second_list содержат одни и тежи изменяемые обьекты данных.
# Чтобы изменения, вносимые в первый список (first_list), не затрагивали второй (second_list), необходимо создать второй список с помощью метода second_list = copy.deepcopy(first_list)

# Решение:
# second_list_new = copy.deepcopy(first_list)
print(second_list_new)