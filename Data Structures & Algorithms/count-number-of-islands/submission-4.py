class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()

        islands = 0
        def bfs(r, c):
            q = deque([(r,c)])
            visit.add((r,c))
            while q:
                r, c = q.popleft()
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    row, col = r+dr, c+dc
                    if (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                        if grid[row][col] == "1" and (row, col) not in visit:
                            q.append((row,col))
                            visit.add((row,col))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1

        return islands
        
        
        
