def isBrightest(grid, x, y):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Neighboring positions (up, down, left, right)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # Check if neighbor exists and compare brightness
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] >= grid[x][y]:
            return False
    return True

def findPixel(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if isBrightest(grid, i, j):
                return (i, j)
    return (-1, -1)

# Test case with the new grid
grid = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 10, 8],
    [5, 6, 7, 20, 9]
]
brightest_pixel = findPixel(grid)
print("Brightest pixel location: ", brightest_pixel)
