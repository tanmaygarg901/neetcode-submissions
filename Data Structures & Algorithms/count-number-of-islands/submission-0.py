class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if (row in range(len(grid)) and
                    col in range(len(grid[0])) and
                    (row,col) not in visited and
                    grid[row][col] == "1"):
                        q.append((row,col))
                        visited.add((row,col))


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        
        return islands