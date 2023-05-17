import random
import threading
import time
from collections import defaultdict

class SomethingWithEvent:

    def __init__(self):
        self.events = defaultdict(dict)
        self._lock = threading.Lock()

    def add_handler(self, f, v: int):
        with self._lock:
            self._events[f][v] = v

    @property
    def get_events(self):
        return self._events

def worker(event_thread: SomethingWithEvent, f, v: int):
    time.sleep(random.randint(1, 3))
    event_thread.add_handler(f, v)

event_thread = SomethingWithEvent()
for i in range(5):
    t = threading.Thread(target=worker, args=(event_thread, lambda x: x+1, i))
    t.start()
main_thread = threading.main_thread()
[t.join() for t in threading.enumerate() if t is not main_thread]

print(event_thread.get_events)
