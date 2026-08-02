class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = "".join([i.lower() for i in s if i.isalnum()])
        return stripped == stripped[::-1]