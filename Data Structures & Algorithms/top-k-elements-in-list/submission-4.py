class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        return sorted(freq, key=freq.get, reverse=True)[0:k]
        