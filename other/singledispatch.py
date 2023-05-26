from functools import singledispatch

@singledispatch
def fun(arg):
    print('unknown')

@fun.register
def _(arg: int | float):
    print('number')

@fun.register
def _(arg: str):
    print('string')

if __name__ == "__main__":
    fun(2)
