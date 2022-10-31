import threading
from queue import Queue


class ThreadBot(threading.Thread):  # ThreadBot является подклассом потока.
    def __init__(self):
        super().__init__(target=self.manage_table)  # Целевой функцией является метод manage_table(), определяемый ниже.
        self.cutlery = Cutlery(knives=0, forks=0)(3)
        self.tasks = Queue()(4)

    def manage_table(self):
        while True:
            task = self.tasks.get()
            if task == 'prepare table':
                kitchen.give(to=self.cutlery, knives=4, forks=4)(6)
            elif task == 'clear table':
                self.cutlery.give(to=kitchen, knives=4, forks=4)
            elif task == 'shutdown':
                return