class Queue:
    def __init__(self, n):
        self.queue = [None]*n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0


    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1

    def pop(self):
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

q = Queue(3)

q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.pop()
q.pop()

"""Плюсы применения циклического буфера на на заданном массиве:
 1. То что зараннее длина(емкость) буфера известна,массив заранее выделен с фиксированным рамером,
  что позовляет эффективно использовать память.
 2. Эффективные операции добавление и удаление элментов, выполняются за констаное время O(1).
 Минусы:
 1. Ограниченная емкость: массив имеет фиксированнвый размер, который определяется при создании 
 экземпляра класса.
"""