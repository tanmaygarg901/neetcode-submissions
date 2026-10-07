class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if (row in range(len(grid)) and
                    col in range(len(grid[0])) and
                    grid[row][col] == "1" and 
                    (row,col) not in visited):
                        queue.append((row,col))
                        visited.add((row,col))
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        
        return islands