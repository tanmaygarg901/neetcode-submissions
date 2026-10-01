class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for i in nums:
            if i-1 not in nums:
                curr = i
                length = 1
                while (curr+1) in nums:
                    curr += 1
                    length += 1
                res = max(length, res)
                
        return res