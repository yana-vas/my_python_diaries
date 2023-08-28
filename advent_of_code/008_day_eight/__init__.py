grid = [list(map(int, line)) for line in open('input_data.txt').read().splitlines()]

visible_trees = 0
scenic_scores = []
for r in range(len(grid)):
    for c in range(len(grid[r])):
        k = grid[r][c]
        L = R = U = D = 0

        for x in range(c - 1, -1, -1):
            L += 1
            if grid[r][x] >= k:
                break

        for x in range(c + 1, len(grid[r])):
            R += 1
            if grid[r][x] >= k:
                break

        for x in range(r - 1, -1, -1):
            U += 1
            if grid[x][c] >= k:
                break

        for x in range(r + 1, len(grid[r])):
            D += 1
            if grid[x][c] >= k:
                break

        # First part
        if all(grid[r][x] < k for x in range(c)) or \
                all(grid[r][x] < k for x in range(c + 1, len(grid[r]))) or \
                all(grid[x][c] < k for x in range(r)) or \
                all(grid[x][c] < k for x in range(r + 1, len(grid))):
            visible_trees += 1
        scenic_scores.append(U * D * L * R)

print(visible_trees)
print(max(scenic_scores))