class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_map = {')':'(', ']':'[', '}':'{'}

        for i in s:
            if i in par_map:
                if stack and stack[-1] == par_map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if stack:
            return False
        else:
            return True

            