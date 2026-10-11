class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for i in nums:
            heapq.heappush_max(self.heap, i)

    def add(self, val: int) -> int:
        heapq.heappush_max(self.heap, val)
        return heapq.nlargest(self.k, self.heap)[-1]
