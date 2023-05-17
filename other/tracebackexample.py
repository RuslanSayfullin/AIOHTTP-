import traceback

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        traceback.print_exc()
    else:
        return result

def main():
    a = 10 
    b = 0
    result = divide(a, b)
    print("Result: ", result)

if __name__ == '__main__':
    main()
