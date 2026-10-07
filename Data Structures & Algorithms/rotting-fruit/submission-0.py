class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        time, fresh = 0, 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r,c])
        
        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        while len(queue) > 0 and fresh > 0:
            for rotten in range(len(queue)):
                r, c = queue.popleft()
                visited.add((r,c))
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if (new_r in range(len(grid))
                    and new_c in range(len(grid[0])) and
                    (new_r, new_c) not in visited and
                    grid[new_r][new_c] == 1):
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        queue.append([new_r,new_c])
            time += 1
        
        return time if fresh == 0 else -1

