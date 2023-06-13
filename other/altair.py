import altair as alt
import pandas as pd

# Создаем набор данных
data = pd.DataFrame({
    'Fruit': ['Apple', 'Banana', 'Cherry'],
    'Price': [1.2, 0.9, 1.5],
    'Quantity': [7, 5, 3]
})

# создаем график
chart = alt.Chart(data).mark_bar().encode(
        x='Fruit',
        y='Price',
        color='Fruit'
)

# сохраняем график
chart.save('chart.html')
