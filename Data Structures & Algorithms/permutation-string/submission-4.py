class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map, s2_map = defaultdict(int), defaultdict(int)
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        for i in s1:
            s1_map[i] += 1
        for j in range(n1):
            s2_map[s2[j]] += 1

        if s1_map == s2_map:
            return True
        
        for i in range(n1, n2):
            s2_map[s2[i]] += 1
            
            left = s2[i - n1]
            s2_map[left] -= 1
            
            if s2_map[left] == 0:
                del s2_map[left]
            
            if s1_map == s2_map:
                return True
            

        return False
        