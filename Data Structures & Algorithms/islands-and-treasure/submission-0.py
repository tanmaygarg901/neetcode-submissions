class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        q = deque()
        visit = set()
        l = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0 and (r,c) not in visit:
                    q.append((r,c))
                    visit.add((r,c))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = l
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    row, col = r+dr, c+dc
                    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                        if grid[row][col] == INF and (row,col) not in visit:
                            q.append((row,col))
                            visit.add((row,col))
            l += 1

        return