class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._size = 0
        self.fixed_array = [None] * self.capacity

    def get(self, i: int) -> int:
        if i < 0 or i >= self._size:
            raise IndexError('Index out of bounds')
        return self.fixed_array[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self._size:
            raise IndexError('Index out of bounds')
        self.fixed_array[i] = n

    def pushback(self, n: int) -> None:
        if self._size == self.capacity:
            self.resize()
        self.fixed_array[self._size] = n
        self._size += 1


    def popback(self) -> int:
        if self._size == 0:
            raise IndexError('Pop from empty array')
        self._size -= 1
        return self.fixed_array[self._size]

    def resize(self) -> None:
        new_fixed_size_arr = [None] * self.capacity * 2
        for i in range(self._size):
            new_fixed_size_arr[i] = self.fixed_array[i]
        self.fixed_array = new_fixed_size_arr
        self.capacity = self.capacity * 2


    def getSize(self) -> int:
        return self._size
        
    
    def getCapacity(self) -> int:
        return self.capacity