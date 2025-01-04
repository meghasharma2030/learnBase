class DeQueue():
    def __init__(self):
        self.list = []

    def push_right(self, element):
        self.list.append(element)

    def push_left(self, element):
        self.list = [element] + self.list

    def pop_right(self):
        if(self.isEmpty()): return None
        else:
            return self.list.pop()

    def pop_left(self):
        if(self.isEmpty()): return None
        else:
            item = self.list[0]
            del self.list[0]
            return item

    def isEmpty(self):
        if(len(self.list) == 0): return True
        return False

    def peek(self):
        return self.list[0]
    


def tryItOut():
    queue = DeQueue()
    print("isEmpty: ",queue.isEmpty())
    queue.push_right(1)
    queue.push_right(2)
    queue.push_right(3)
    queue.push_right(4)
    queue.push_right(5)
    print("push_right:  ", queue.list)
    print("pop_left:  ", queue.pop_left(), queue.list)
    print("peek: ",queue.peek())
    print("isEmpty: ",queue.isEmpty())

tryItOut()