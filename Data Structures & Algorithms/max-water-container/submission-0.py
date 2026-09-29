class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1
        while l < r:
            curr_area = min(heights[l], heights[r]) * (r-l)
            if curr_area > res:
                res = curr_area
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return res