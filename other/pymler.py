from pymler import summary, muppy

# создаем список из 1 миллиона строк
list_of_strings = ['hello world']*1000000

# получаем текущее состояние памяти
all_objects = muppy.get_ojects()

# создаем отчет по памяти
sum1 = summary.summarize(all_objects)
summary.print_(sum1)

# удаляем список из памяти
del list_of_strings

# получаем новое текущее состояние памяти
all_objects = muppy.get_objects()

# создаем новый отчет по памяти
sum2 = summary.sumarize(all_objects)
summary.print_(sum2)
