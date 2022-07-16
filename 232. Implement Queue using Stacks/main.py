class MyQueue:
    def __init__(self):
        self.stack1, self.stack2 = [], []
        self.front = None

    def push(self, x: int) -> None:
        if self.empty():
            self.stack1.append(x)
        else:
            while not self.empty():
                self.stack2.append(self.stack1.pop())
            self.stack1.append(x)
            while len(self.stack2) > 0:
                self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        if not self.empty():
            return self.stack1.pop()

    def peek(self) -> int:
        if not self.empty():
            return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0


obj = MyQueue()
obj.push(10)
print(obj.peek())
print(obj.pop())
print(obj.pop())

