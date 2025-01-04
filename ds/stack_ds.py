class Stack():
    def __init__(self):
        self.list = []

    def push(self, element):
        self.list.append(element)

    def pop(self):
        if(self.isEmpty()): return None
        else:
            return self.list.pop()

    def isEmpty(self):
        if(len(self.list) == 0): return True
        return False

    def peek(self):
        return self.list[len(self.list)-1]
    


def tryItOut():
    stack = Stack()
    print("isEmpty: ",stack.isEmpty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print("push:  ", stack.list)
    print("pop:  ", stack.pop(), stack.list)
    print("peek: ",stack.peek())
    print("isEmpty: ",stack.isEmpty())

tryItOut()