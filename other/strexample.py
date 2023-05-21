class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year =year

    def __str__(self):
        return f"{self.title} ({self.author}, {self.year})"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

# Создание экземпляра класс Book
book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

# Вывод обьекта на кансоль с использованием функции print()
print(book)

# Вызов функции str()
print(str(book))

# Вызов функции repr()
print(repr(book))
