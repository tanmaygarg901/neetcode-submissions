class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0

        def dfs(r,c):
            if (r not in range(len(grid)) or
            c not in range(len(grid[0])) or
            grid[r][c] == 0 or (r,c) in visited):
                return 0

            visited.add((r,c))
            return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1))
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = dfs(r,c)
                    max_area = max(area, max_area)
        
        return max_area



