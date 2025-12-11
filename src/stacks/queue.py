class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x: int) -> None:
        self.in_stack.append(x)

    def dequeue(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            return None
        return self.out_stack.pop()
    
    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            return None
        return self.out_stack[-1]
