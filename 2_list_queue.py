class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def is_empty(self):
        return len(self.buffer) == 0

    def is_full(self):
        return len(self.buffer) == self.capacity

    def enqueue(self, item):
        if self.is_full():
            self.buffer.pop(0)
        self.buffer.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.buffer.pop(0)


q = Queue(4)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
q.dequeue()
q.enqueue(6)

"""Плюсы применения циклического буфера на на заданном массиве:
    1. Не сложен в реализации, спользование встроенного списка. 
   Минусы:
    1. Большое количетсво операций, при добавлении нового,если список уже заполнен
    ,старый элемент удаляется из начала списка, что требует сдвига всех остальных элементов.
    2. Худшая производительность: операция удаления элемента из начала списка имеет сложность O(n), 
    где n - размер списка.
"""