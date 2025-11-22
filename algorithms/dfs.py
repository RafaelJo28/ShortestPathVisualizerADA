def dfs(grid, start, end):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()

        if node == end:
            return visited, path

        if node in visited:
            continue

        visited.add(node)

        for neighbor in grid.get_neighbors(node):
            if neighbor not in visited and not neighbor.is_obstacle:
                stack.append((neighbor, path + [neighbor]))

    return visited, None  # No path found