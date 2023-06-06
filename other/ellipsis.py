print(... is Ellipsis)  # True

# Исключение без тела. 
class CustomException(Exception):
    ...

def tuple_sum(t: tuple[int, ...]) -> int:
    return sum(t)

tuple_sum((1, 2))
tuple_sum((1, 2, 3))
tuple_sum(())

# Предуприждение линтера
tuple_sum(('h'))
tuple_sum((1, 2, 3, 'h'))
tuple_sum([1, 2, 3])
