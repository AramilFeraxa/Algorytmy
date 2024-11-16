class Stack:
    def __init__(self, max_size=5):
        self.stack = []
        self.top = -1
        self.max_size = max_size

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top + 1 == self.max_size

    def push(self, element):
        if self.is_full():
            print("Stos jest pełny! Nie można dodać elementu.")
            return
        else:
            self.top += 1
            if self.top < len(self.stack):
                self.stack[self.top] = element
            else:
                self.stack += [element]
        print("Dodano element: ", element)

    def pop(self):
        if self.is_empty():
            print("Stos jest pusty! Nie można usunąć elementu.")
            return None
        else:
            element = self.stack[self.top]
            self.top -= 1
            print("Usunięto element: ", element)

    def peek(self):
        if self.is_empty():
            print("Stos jest pusty!")
            return None
        else:
            print("Wierzchni element: ", self.stack[self.top])

    def size(self):
        print("Rozmiar stosu: ", self.top + 1)

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

stack.peek()
stack.pop()
stack.peek()
stack.size()