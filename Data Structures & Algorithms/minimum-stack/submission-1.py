class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # If stack is empty, val is the min. 
        # Otherwise, compare val with the min of the current top element.
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        raise IndexError("pop from empty stack")

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        raise IndexError("getMin from empty stack")