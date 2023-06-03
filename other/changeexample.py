from collections import deque
from math import sqrt

class Compose:
    def __init__(self):
        self._funcs = deque()

    def _call__(self, *args, **kwargs):
        result = None
        for f in self._funcs:
            result = f(*args, **kwargs)
            args = [result]
            kwargs = dict()
        return result

    def __rshift__(self, f):
        self._funcs.append(f)
        return self

    def __lshift__(self, f):
        self._funcs.appendleft(f)
        return self

sqrt_abs = (Compose() << sqrt << abs)
sqrt_abs2 = (Compose() >> abs >> sqrt)

print(sqrt_abs(-9)) 
print(sqrt_abs2(-9))
