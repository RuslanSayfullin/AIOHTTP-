import threading

def func():
    for i in range(10):
        print("hello from thread")

thread = threading.Thread(target=func)
thread.start()
