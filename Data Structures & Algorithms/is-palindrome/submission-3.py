class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = -1
        cleaned = "".join([i.lower() for i in s if i.isalnum()])
        while l < len(cleaned)//2:
            if cleaned[l] != cleaned[r]:
                return False
            l += 1
            r -= 1
        return True
