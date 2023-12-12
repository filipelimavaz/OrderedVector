# OrderedVector 📋

## Description
This is an example implementation of an ordered vector in Python for the Data Structures course. The code presents a class called `OrderedVector`, which allows the creation and manipulation of an ordered vector with a defined capacity.

## Features
The `OrderedVector` class has the following features:

### 1. Initialization
```python
import numpy as np

class OrderedVector:

    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.value_list = np.empty(self.capacity, dtype=int)

Initializes an ordered vector with the specified capacity.```

### 2. Printing

def print(self):
        if self.last_position == -1:
            print('List is empty')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.value_list[i]

Prints the elements of the vector.

### 3. Add

def add(self, value):
        if self.last_position == self.capacity - 1:
            print('Maximum capacity reached')
            return
        
        position = 0
        for i in range(self.last_position + 1):
            position = 1
            if self.value_list[i] > value:
                break
            if i == self.last_position:
                position = i + 1

        x = self.last_position
        while x >= position:
            self.value_list[x + 1] = self.value_list[i]
            x -= 1
        
        self.value_list[position] = value
        self.last_position += 1

Adds an element to the vector, maintaining ascending order.

### Notes

- If the maximum capacity is reached, a message indicating that the maximum capacity has been reached will be displayed.
- The class uses the NumPy library for creating the vector.

