from fastcore.utils import *
from fastcore.foundation import L

# Создаём списое чисел
def is_even(x):
    return x % 2 ==0

# Используем функцию 'partition' из Fastcore для разделения списка на четные и нечетные числа
even_numbers, odd_numbers = partition(is_even, numbers)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

