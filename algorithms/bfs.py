from collections import deque


def reconstruct_path(came_from, end):
    path = [end]
    while end in came_from:
        end = came_from[end]
        path.append(end)
    return path[::-1]


def bfs(grid, start, end):
    queue = deque([start])
    visited = {start}
    came_from = {}

    while queue:
        current = queue.popleft()

        if current == end:
            return visited, reconstruct_path(came_from, current)

        for neighbor in grid.get_neighbors(current):
            if neighbor in visited or neighbor.is_obstacle:
                continue

            visited.add(neighbor)
            came_from[neighbor] = current
            queue.append(neighbor)

    return visited, None
