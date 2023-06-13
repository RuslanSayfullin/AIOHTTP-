from tabulate import tabulate

data = [
        ["Apple", 1.2, 7],
        ["Banana", 0.9, 5],
        ["Cherry", 1.5, 3]
]

headers = ["Fruit", "Price", "Quantity"]

print(tabulate(data, headers=headers, tablefmt="grid"))
