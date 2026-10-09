class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[course].append(pre)
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if adj[crs] == []:
                return True
            visit.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            adj[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
        

        

