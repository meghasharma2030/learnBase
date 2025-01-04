class Heap():
    def __init__(self):
        self.heap = []
        self.type = "min"

    def generate_min_heap(self, arr):
        self.type = "min"
        self.heap = self.__buildHeap(arr)

    def generate_max_heap(self, arr):
        self.type = "max"
        self.heap = self.__buildHeap(arr)

    def __buildHeap(self, array):
        midIndex = len(array)//2
        for i in reversed(range(0, midIndex)):
            if(self.type == "min"): self.__min_heapify(array, i)
            else: self.__max_heapify(array, i)
        return array

    def __min_heapify(self, array, index):
        leftIndex = 2*index + 1
        rightIndex = 2*index + 2
        smallIndex = index

        if((leftIndex < len(array)) and array[leftIndex] < array[smallIndex]):
            smallIndex = leftIndex
        if((rightIndex < len(array)) and array[rightIndex] < array[smallIndex]):
            smallIndex = rightIndex

        if(smallIndex != index):
            array[smallIndex], array[index] = array[index], array[smallIndex]
            self.__min_heapify(array, smallIndex)
            
    def __max_heapify(self, array, index):
        leftIndex = 2*index + 1
        rightIndex = 2*index + 2
        largeIndex = index

        if((leftIndex < len(array)) and array[leftIndex] > array[largeIndex]):
            largeIndex = leftIndex
        if((rightIndex < len(array)) and array[rightIndex] > array[largeIndex]):
            largeIndex = rightIndex

        if(largeIndex != index):
            array[largeIndex], array[index] = array[index], array[largeIndex]
            self.__max_heapify(array, largeIndex)

    def max_push(self, element):
        self.heap.append(element)
        eleIndex = len(self.heap)-1
        parentIndex = (eleIndex-1)//2
        while (eleIndex > 0 and self.heap[parentIndex] < self.heap[eleIndex]):
            self.heap[parentIndex], self.heap[eleIndex] = self.heap[eleIndex], self.heap[parentIndex]
            eleIndex = parentIndex
            parentIndex = (eleIndex-1)//2

    def min_push(self, element):
        self.heap.append(element)
        eleIndex = len(self.heap)-1
        parentIndex = (eleIndex-1)//2
        while (eleIndex > 0 and self.heap[parentIndex] > self.heap[eleIndex]):
            self.heap[parentIndex], self.heap[eleIndex] = self.heap[eleIndex], self.heap[parentIndex]
            eleIndex = parentIndex
            parentIndex = (eleIndex-1)//2

    def pop(self):
        if(len(self.heap) > 1):
            self.heap[0] = self.heap[len(self.heap)-1]
            del self.heap[len(self.heap)-1]
            if(self.type == "min"): self.__min_heapify(self.heap, 0)
            else: self.__max_heapify(self.heap, 0)

    def peek(self):
        return self.heap[0]


def tryItOut():
    heapData = Heap()
    heapData.generate_min_heap([40, 30, 15, 10, 20])
    print("init",heapData.heap)
    heapData.pop()
    print("pop",heapData.heap)
    heapData.min_push(40)
    print("push",heapData.heap)
    print("peep",heapData.peek())


tryItOut()