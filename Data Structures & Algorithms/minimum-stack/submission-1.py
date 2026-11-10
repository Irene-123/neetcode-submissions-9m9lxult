class MinStack:

    def __init__(self):
        self.stack = []   
        self.minStack = []

    def push(self, val: int) -> None:
        if self.minStack:
            new_minimum = min(val, self.minStack[-1])
        else:
            new_minimum = val
        self.stack.append(val)
        self.minStack.append(new_minimum)

    def pop(self) -> None:
        val = self.stack[-1]
        del self.stack[-1]
        del self.minStack[-1]
        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
