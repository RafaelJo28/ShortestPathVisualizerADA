import heapq
import itertools

counter = itertools.count()


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]


def dijkstra(grid, start, end):
    heap = [(0, next(counter), start)]
    came_from = {}
    distances = {start: 0}
    visited = set()

    while heap:
        current_cost, _, current = heapq.heappop(heap)

        if current in visited:
            continue

        visited.add(current)

        if current == end:
            return visited, reconstruct_path(came_from, current)

        for neighbor in grid.get_neighbors(current):
            if neighbor.is_obstacle:
                continue

            new_cost = distances[current] + neighbor.cost + neighbor.delay

            if neighbor not in distances or new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                came_from[neighbor] = current
                heapq.heappush(heap, (new_cost, next(counter), neighbor))

    return visited, None
