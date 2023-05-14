from datetime import datetime

# задаем дату, до которой нужно посчитать количество дне
date_str = '2023-12-31'
end_date = datetime.strptime(date_str, '%Y-%m-%d')

# вычесляем текущую дату
today = datetime.today()

# вычисляем разницу между датами в днях
days_left = (end_date - today).days

# выводим результат
print(f'Осталось {days_left} дней до {date_str}')
