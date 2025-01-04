class Sort():
    def __init__(self):
        pass

    def merge_sort(self, arr):
        if(len(arr) <= 1): return arr
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        self.merge_sort(left_arr)
        self.merge_sort(right_arr)
        self.__merge(arr, left_arr, right_arr)

    def __merge(self, arr, left_arr, right_arr):
        i = 0; j = 0; k = 0
        while i < len(left_arr) and j < len(right_arr):
            if(left_arr[i] < right_arr[j]):
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    def heap_sort(self, arr):
        self.__create_max_heap(arr)
        for i in reversed(range(0, len(arr))):
            arr[i], arr[0] = arr[0], arr[i]
            self.__max_heapify(arr, 0, i)

    def __create_max_heap(self, array):
        for i in reversed(range(0, len(array)//2)):
            self.__max_heapify(array, i, len(array))

    def __max_heapify(self, array, index, size):
        leftIndex = 2*index + 1
        rightIndex = 2*index + 2
        largeIndex = index

        if((leftIndex < size) and array[leftIndex] > array[largeIndex]):
            largeIndex = leftIndex
        if((rightIndex < size) and array[rightIndex] > array[largeIndex]):
            largeIndex = rightIndex

        if(largeIndex != index):
            array[largeIndex], array[index] = array[index], array[largeIndex]
            self.__max_heapify(array, largeIndex, size)

    # Each iteration gives one largest element. 
    # Can be used for finding kth largest element  
    def bubble_sort(self, arr):
        for i in range(0, len(arr)-1):
            isSorted = True
            for j in range(0, (len(arr)-1-i)):
                if(arr[j+1] < arr[j]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    isSorted = False
            if(isSorted): break

    # best for linked list sorting, as insertion takes O(n)
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
                key = arr[i]
                j = i-1
                while j >= 0 and key < arr[j]:
                    arr[j+1] = arr[j]
                    j -= 1
                arr[j+1] = key

    def selection_sort(self, arr):
        for i in range(0, len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                if(arr[j] < arr[min_index]):
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

    def quick_sort(self, arr, low=None, high=None):
        if(low == None and high == None):
            low = 0; high = len(arr)-1
        if(low < high):
            pi = self.__quick_partition(arr, low, high)
            self.quick_sort(arr, low, pi)
            self.quick_sort(arr, pi+1, high)

    def __quick_partition(self, arr, low, high):
        pivot = arr[low]
        i = low; j = high
        while i < j:
            while i < high and arr[i] <= pivot:
                i += 1
            while j > low and arr[j] > pivot:
                j -= 1
            if(i < j):
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j

    def findKthlargestElement(self, arr, k, low=None, high=None):
        if(low == None and high == None):
            low = 0; high = len(arr)-1
        pi = self.__quick_partition(arr, low, high)
        if(pi == len(arr)-k):
            return arr[pi]
        elif(pi < len(arr)-k):
            return self.findKthlargestElement(arr, k, pi+1, high)
        else:
            return self.findKthlargestElement(arr, k, low, pi-1)

def tryItOut():
    array = [9,7,3,17,5,6,4,8,2]
    sort = Sort()
    # sort.merge_sort(array)
    # sort.heap_sort(array)
    # sort.bubble_sort(array)
    # sort.insertion_sort(array)
    # sort.selection_sort(array)
    # sort.quick_sort(array)
    print("sorted_array",array)
    print("kth largest", sort.findKthlargestElement(array, 4))

tryItOut()
