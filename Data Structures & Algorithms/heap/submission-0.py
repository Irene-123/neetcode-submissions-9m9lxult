class MinHeap:
    
    def __init__(self):
        self.heap = []

    def _sift(self, index):
        while True:
            smallest = index
            left, right = index*2 + 1, index*2 + 2
            
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest], self.heap[index]
            )
            index = smallest

    def push(self, val: int) -> None:
        self.heap.append(val)

        index = len(self.heap) - 1 
        parent = (index - 1)//2

        while index > 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]

            index = parent 
            parent = (index - 1)//2
        

    def pop(self) -> int:

        if not self.heap:
            return -1

        popped_item = self.heap[0]
        last_item = self.heap.pop() 

        if not self.heap:
            return popped_item

        self.heap[0] = last_item
        self._sift(0)

        return popped_item
        

    def top(self) -> int:
        if len(self.heap) > 0:
            return self.heap[0]
        return -1
        

    def heapify(self, nums: List[int]) -> None:
        self.heap = nums.copy()

        for i in range(len(nums)//2-1, -1, -1):
            self._sift(i)

        












        