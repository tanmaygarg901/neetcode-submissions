class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, (val, key))
        heapq.heapify_max(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop_max(heap)[1])
        return res
