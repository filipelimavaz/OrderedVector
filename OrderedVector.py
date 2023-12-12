import numpy as np

class OrderedVector:

    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.valor_list = np.empty(self.capacity, dtype=int)

    def print(self):
        if self.last_position == -1:
            print('List is empty')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.valor_list[i])

    def add(self, valor):
        if self.last_position == self.capacity - 1:
            print('Maximum capacity reached')
            return
        
        position = 0
        for i in range(self.last_position + 1):
            position = 1
            if self.valor_list[i] > valor:
                break
            if i == self.last_position:
                position = i + 1

        x = self.last_position
        while x >= position:
            self.valor_list[x + 1] = self.valor_list[i]
            x -= 1
        
        self.valor_list[position] = valor
        self.last_position += 1

list = OrderedVector(10)
list.add(5)
list.add(9)
list.add(1)
list.print()
