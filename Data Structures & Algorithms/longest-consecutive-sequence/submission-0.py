class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        max_len = 0
        for i in num:
            curr = i
            length = 1
            if i-1 in num:
                continue
            while curr+1 in num:
                length += 1
                curr += 1
            max_len = max(length, max_len)
        return max_len
