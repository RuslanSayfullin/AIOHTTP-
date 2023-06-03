# так выглядит chain
def chain(*iterables):
    # chain('ABC', 'DEF') -> A B C D E F
    for it in iterables:
        for element in it:
            yield element

lst = [[1], [2], [3]]

print(*chain(*lst))
# после распоковки будет выглядить как
# chain([1], [2], [3])
# print(1, 2, 3)

print(*chain(lst))
# [1], [2], [3]

print(chain(lst))
# <generator ....
