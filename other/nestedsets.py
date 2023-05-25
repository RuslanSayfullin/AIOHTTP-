class Category:
    def __init__(self, id, name, left, right):
        self.id = id
        self.name = name
        self.left = left
        self.right = right

category1 = Category(1, 'Компьютеры', 1, 14)
category2 = Category(2, 'Ноутбуки', 2, 7)
category3 = Category(3, 'Ультрабуки', 3, 4)
category4 = Category(4, 'Игровые ноутбуки', 5, 6)
category5 = Category(5, ' ПК', 8, 13)
category6 = Category(6, 'Настольные ПК', 9, 10)
category7 = Category(7, 'Моноблоки', 11, 12)
category8 = Category(8, 'Электроника', 15, 22)
category9 = Category(9, 'Смартфоны', 16, 17)
category10 = Category(10, 'Телевизоры', 18, 21)
category11 = Category(11, 'ЖК-телевизоры', 19, 20)
category12 = Category(12, 'Oled-телевизоры', 23, 24)

def get_descendants(category, categories):
    descendants = []
    for cat in categories:
        if cat.left > category.left and cat.right < category.right:
            descendants.append(cat)
        return descendants

if __name__ == "__main__":
    descendants = get_descendants(category1, [category2, category2, category3, category4, category5, category6, category7, category8, category9, category10, category11, category12])

    for descendant in descendants:
        print(descendant.name)



