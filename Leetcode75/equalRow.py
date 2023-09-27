class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        column = [grid[c] for c in range(len(grid[0]))]
        for i in range(len(grid)):
            if grid[i] in column:
                count += column.count(grid[i])
        return count
