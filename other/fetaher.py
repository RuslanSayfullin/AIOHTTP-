import pandas as pd
import feather

# Создаем пример таблицы данных
data = {
    'coll': [1, 2, 3, 4],
    '2': ['A', 'B', 'C', 'D'],
    'col3': [1.1, 2.2, 3.3, 4.4]
}

df = pd.DataFrame(data)

# Записываем таблицу данных в файл формата Feather
feather.write_dataframe(df, 'ecample.feather')

# Читаем таблицу данных из формата Feather
read_df = feather.read_dataframe('example.feather')
print(read_df)
