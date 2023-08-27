import os

old_name = "/tmp/file.txt"
new_name = "/tmp/renamed_file.txt"

try:
    os.rename(old_name, new_name)
    print(f"Переименование из {old_name} и {new_name} прошло успешно")
except FileNotFoundError:
    print(f"Файл {old_name} не найден")

print(os.listdir('/tmp'))

