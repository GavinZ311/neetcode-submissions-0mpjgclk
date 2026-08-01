class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.table = [None] * capacity
    
    def hash(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        head = self.table[index]

        if not head:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            prev = None
            curr = head
            while curr:
                if curr.key == key:
                    curr.value = value
                    return
                prev, curr = curr, curr.next
            prev.next = Node(key, value)
            self.size += 1
        
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash(key)
        head = self.table[index]

        while head != None:
            if head.key == key:
                return head.value
            head = head.next
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)
        head = self.table[index]
        prev = None
        while head:
            if head.key == key:
                if prev:
                    prev.next = head.next
                else:
                    self.table[index] = head.next
                self.size -= 1
                return True

            prev, head = head, head.next

        return False


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for node in old_table:
            while node:
                self.insert(node.key, node.value)
                node = node.next