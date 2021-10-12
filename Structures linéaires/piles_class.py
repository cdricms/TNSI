class Stack:
    stack = []
    length = 0

    def __init__(self, stack=[]):
        self.stack = stack
        self.length = len(stack)

    def push(self, el):
        self.stack += [el]
        self.length += 1
        return self.stack

    def pop(self):
        if self.length == 0:
            return 0

        self.stack.pop()
        self.length -= 1
        return self.stack[-1]

    def top(self):
        if self.length == 0:
            return None
        return self.stack[-1]


def main():
    stack = Stack()
    stack.pop()
    print(stack.top())
    print(stack.stack)

    stack.push(5)
    stack.push(10)
    print(stack.stack)
    print(stack.length)

    stack.pop()
    print(stack.stack)

    print(stack.length)


if __name__ == "__main__":
    main()
