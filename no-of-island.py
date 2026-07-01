class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        count = 0

        # Traverse every cell
        for i in range(rows):
            for j in range(cols):

                # Found an unvisited land cell
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)

        return count

    # Depth First Search
    def dfs(self, grid, i, j):

        # Base case:
        # 1. Out of bounds
        # 2. Water ('0')
        if (i < 0 or j < 0 or
            i >= len(grid) or
            j >= len(grid[0]) or
            grid[i][j] == "0"):
            return

        # Mark current land as visited
        grid[i][j] = "0"

        # Explore all four directions
        self.dfs(grid, i + 1, j)  # Down
        self.dfs(grid, i - 1, j)  # Up
        self.dfs(grid, i, j + 1)  # Right
        self.dfs(grid, i, j - 1)  # Left
