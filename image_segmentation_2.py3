def dfs(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != '1':
        return
    grid[x][y] = '0'  # Mark the cell as visited
    # Explore all eight possible directions
    dfs(grid, x+1, y)
    dfs(grid, x-1, y)
    dfs(grid, x, y+1)
    dfs(grid, x, y-1)
    dfs(grid, x+1, y+1)
    dfs(grid, x-1, y-1)
    dfs(grid, x+1, y-1)
    dfs(grid, x-1, y+1)

def count_connected_components(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count

# Example grid from the assignment
grid = [
    "000110001010",
    "111011110001",
    "111010010010",
    "100000000100"
]
# Convert the grid to a list of lists for easier manipulation
grid = [list(row) for row in grid]

# Call the function and print the result
print(count_connected_components(grid))
