import heapq

class MedianOfAnIntegerStream:
    def __init__(self):
        # size(min_heap) == size(max_heap) OR size(min_heap) + 1 = size(max_heap)
        # elemenets > median
        self.min_heap = []
        # elements < median
        self.max_heap = []

    def add(self, num: int) -> None:
        if not self.max_heap:
            self.max_heap.append(-num)    
            print
            return    
        
        if len(self.max_heap) == len(self.min_heap):
            # add to max_heap
            if num > self.min_heap[0]:
                temp = heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, num)
                num = temp 
            heapq.heappush(self.max_heap, -num)
            return 
        # add to min_heap
        if num < -self.max_heap[0]:
            temp = -heapq.heappop(self.max_heap)
            heapq.heappush(self.max_heap, -num)
            num = temp
        heapq.heappush(self.min_heap, num)

    def get_median(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2

