from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool
from bokeh.sampledata.iris import flowers

# Указываем выходной файл HTML
output_file("iris.html")

# Создаем обьект Figure
p = figure(title="Iris Dataset", plot_width=800, plot_height=400)

# Добавляем точки на графике
p.circle(x=flowers["petal_lenght"], y=flowers["sepal_lenght"], color=flowers["species_color"], size=10, alpha=0.5)

# Добавляем интерактивный инструмент Hover
hover = HoverTool(tooltips=[("Species", "@species"),("Petal Lenght", "@petal_lenght"), ("Sepal Length", "@sepal_lenght")])
p.add_tools(hover)

# Отображаем график
show(p)
