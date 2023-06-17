import theano
import numpy as np

# Создадим символические переменные
x = theano.tensor.fmatrix('x')
y= theano.tensor.dot(x, y)

# Создадим функцию для вычисления матричного умножения
multipl = theano.function([x, y], z)

# Создаем две матрицы
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Вычисляем произведение матриц с помощью Theano
result = multiply(a, b)
print(result)
