class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            if self.minStack[-1]>=val:
                self.minStack.append(val)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack and self.minStack:
            if self.minStack[-1] == self.stack.pop():
                del self.minStack[-1]
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return 0
