import heapq
import itertools

# Unique counter for heap tie-breaking
counter = itertools.count()

def manhattan(a, b):
    # Manhattan distance heuristic for A* on a grid
    return abs(a.row - b.row) + abs(a.col - b.col)


def reconstruct_path(came_from, current):
    # Reconstruct final path from end to start
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]


def astar(grid, start, end):
    open_set = []
    heapq.heappush(open_set, (0, next(counter), start))

    came_from = {}
    g_score = {start: 0}

    visited = set()

    while open_set:
        _, _, current = heapq.heappop(open_set)

        if current == end:
            return visited, reconstruct_path(came_from, current)

        visited.add(current)

        for neighbor in grid.get_neighbors(current):

            if neighbor.is_obstacle:
                continue

            # Base movement cost + delay
            tentative_g = g_score[current] + neighbor.cost + neighbor.delay

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                f_score = tentative_g + manhattan(neighbor, end)
                heapq.heappush(open_set, (f_score, next(counter), neighbor))

    return visited, None