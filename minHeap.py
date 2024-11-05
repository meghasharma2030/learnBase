class MinHeap:
    def __init__(self, array):
        self.heap = []
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        midIndex = len(array)//2
        for i in reversed(range(0, midIndex)):
            self.heapify(array, i)
        return array

    def heapify(self, array, index):
        leftIndex = 2*index + 1
        rightIndex = 2*index + 2
        largeIndex = index

        if((leftIndex < len(array)) and array[leftIndex] < array[largeIndex]):
            largeIndex = leftIndex
        if((rightIndex < len(array)) and array[rightIndex] < array[largeIndex]):
            largeIndex = rightIndex

        if(largeIndex != index):
            array[largeIndex], array[index] = array[index], array[largeIndex]
            self.heapify(array, largeIndex)
    
    def push(self, element):
        self.heap.append(element)
        eleIndex = len(self.heap)-1
        parentIndex = (eleIndex-1)//2
        while (eleIndex > 0 and self.heap[parentIndex] < self.heap[eleIndex]):
            self.heap[parentIndex], self.heap[eleIndex] = self.heap[eleIndex], self.heap[parentIndex]
            eleIndex = parentIndex
            parentIndex = (eleIndex-1)//2

    def pop(self):
        if(len(self.heap) > 1):
            self.heap[0] = self.heap[len(self.heap)-1]
            del self.heap[len(self.heap)-1]
            self.heapify(self.heap, 0)

    def peek(self):
        return self.heap[0]


def tryItOut():
    minHeap = MinHeap([40, 30, 15, 10, 20])
    print("init",minHeap.heap)
    minHeap.pop()
    print("pop",minHeap.heap)
    minHeap.push(40)
    print("push",minHeap.heap)
    print("peep",minHeap.peek())


tryItOut()