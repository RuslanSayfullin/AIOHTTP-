import random
import leather

# Создаем список из точек со случайными координатами
dot_data = [(random.randint(0, 250), random.randint(0, 250)) for i in range(100)]

# Функция возвращает строку с цветом в формате RGB, цвет зависит от координат
def colorizer(d):
    return 'rgb(%i,%i,%i)' % (d.x, d.y, 150)

# Создаем график и присваеваем ему название
chart = leather.Chart('Colorized dots')

# Добавляем точки на график
chart.add_dots(dot_data, fill_color=colorizer)

# Сохраняем график в формате .svg
chart.to_svg('charts/colorized_dots.svg')
