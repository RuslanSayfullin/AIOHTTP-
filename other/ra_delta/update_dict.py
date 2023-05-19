# 1.1. Какой вывод мы получим в консоли:
def update_dict(key, value, defaults={}):
    defaults[key] = value
    print(defaults)


update_dict(key='fruit', value='apple')
update_dict(key='vegetable', value='tomato', defaults={'tree': 'oak'})
update_dict(key='car', value='ferrari')

# Вывод:
# {'fruit': 'apple'}
# {'tree': 'oak', 'vegetable': 'tomato'}
# {'fruit': 'apple', 'car': 'ferrari'}


# Исправленное:
def update_dict_new(key: str, value: str, defaults={}) -> dict:
    defaults[key] = value
    print(defaults)
    defaults.clear()


update_dict_new(key='fruit', value='apple')
update_dict_new(key='vegetable', value='tomato', defaults={'tree': 'oak'})
update_dict_new(key='car', value='ferrari')

# Вывод:
# {'fruit': 'apple'}
# {'tree': 'oak', 'vegetable': 'tomato'}
# {'car': 'ferrari'}




