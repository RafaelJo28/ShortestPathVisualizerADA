"""
Pathfinding algorithms that work with tuple-based grid coordinates.
These are wrappers around the core algorithms adapted for the visualizer.
"""
from collections import deque
import heapq
import itertools
import math


def bfs_pathfind(grid, start, end):
    """
    Breadth-First Search - finds shortest path in unweighted grids.
    
    Args:
        grid: 2D list of Node objects
        start: Tuple (row, col) for start position
        end: Tuple (row, col) for end position
    
    Returns:
        Tuple of (visited_list, path_list)
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    queue = deque([start])
    visited = {start}
    came_from = {start: None}
    visited_list = [start]
    
    while queue:
        current = queue.popleft()
        
        if current == end:
            # Reconstruct path
            path = []
            node = end
            while node is not None:
                path.append(node)
                node = came_from[node]
            return visited_list, path[::-1]
        
        # 4-directional movement
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = current[0] + dr, current[1] + dc
            neighbor = (nr, nc)
            
            if (0 <= nr < rows and 0 <= nc < cols and
                neighbor not in visited and
                not grid[nr][nc].is_obstacle):
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)
                visited_list.append(neighbor)
    
    return visited_list, []


def dijkstra_pathfind(grid, start, end):
    """
    Dijkstra's Algorithm - finds shortest path considering edge weights.
    
    Args:
        grid: 2D list of Node objects
        start: Tuple (row, col) for start position
        end: Tuple (row, col) for end position
    
    Returns:
        Tuple of (visited_list, path_list)
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    counter = itertools.count()
    heap = [(0, next(counter), start)]
    came_from = {start: None}
    distances = {start: 0}
    visited = set()
    visited_list = []
    
    while heap:
        current_dist, _, current = heapq.heappop(heap)
        
        if current in visited:
            continue
        
        visited.add(current)
        visited_list.append(current)
        
        if current == end:
            # Reconstruct path
            path = []
            node = end
            while node is not None:
                path.append(node)
                node = came_from[node]
            return visited_list, path[::-1]
        
        r, c = current
        
        # 4-directional movement
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            
            if (0 <= nr < rows and 0 <= nc < cols and
                neighbor not in visited and
                not grid[nr][nc].is_obstacle):
                
                cost = 1 if not hasattr(grid[nr][nc], 'cost') else grid[nr][nc].cost
                new_dist = current_dist + cost
                
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    came_from[neighbor] = current
                    heapq.heappush(heap, (new_dist, next(counter), neighbor))
    
    return visited_list, []


def astar_pathfind(grid, start, end):
    """
    A* Algorithm - finds shortest path with heuristic guidance.
    
    Args:
        grid: 2D list of Node objects
        start: Tuple (row, col) for start position
        end: Tuple (row, col) for end position
    
    Returns:
        Tuple of (visited_list, path_list)
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    def heuristic(pos1, pos2):
        """Manhattan distance heuristic."""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    start_h = heuristic(start, end)
    counter = itertools.count()
    heap = [(start_h, next(counter), start)]
    came_from = {start: None}
    g_score = {start: 0}
    f_score = {start: start_h}
    visited = set()
    visited_list = []
    
    while heap:
        _, _, current = heapq.heappop(heap)
        
        if current in visited:
            continue
        
        visited.add(current)
        visited_list.append(current)
        
        if current == end:
            # Reconstruct path
            path = []
            node = end
            while node is not None:
                path.append(node)
                node = came_from[node]
            return visited_list, path[::-1]
        
        r, c = current
        
        # 4-directional movement
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            
            if (0 <= nr < rows and 0 <= nc < cols and
                neighbor not in visited and
                not grid[nr][nc].is_obstacle):
                
                cost = 1 if not hasattr(grid[nr][nc], 'cost') else grid[nr][nc].cost
                tentative_g = g_score[current] + cost
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    h = heuristic(neighbor, end)
                    f = tentative_g + h
                    f_score[neighbor] = f
                    heapq.heappush(heap, (f, next(counter), neighbor))
    
    return visited_list, []


def dfs_pathfind(grid, start, end):
    """
    Depth-First Search - explores deeply before backtracking.
    
    Args:
        grid: 2D list of Node objects
        start: Tuple (row, col) for start position
        end: Tuple (row, col) for end position
    
    Returns:
        Tuple of (visited_list, path_list)
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    visited = set()
    came_from = {start: None}
    visited_list = []
    
    def dfs(current):
        if current in visited:
            return False
        
        visited.add(current)
        visited_list.append(current)
        
        if current == end:
            return True
        
        r, c = current
        
        # 4-directional movement
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            
            if (0 <= nr < rows and 0 <= nc < cols and
                neighbor not in visited and
                not grid[nr][nc].is_obstacle):
                
                came_from[neighbor] = current
                if dfs(neighbor):
                    return True
        
        return False
    
    if dfs(start):
        # Reconstruct path
        path = []
        node = end
        while node is not None:
            path.append(node)
            node = came_from[node]
        return visited_list, path[::-1]
    
    return visited_list, []


def get_algorithm_function(algorithm_name):
    """Get the algorithm function by name."""
    algorithms = {
        "BFS": bfs_pathfind,
        "Dijkstra": dijkstra_pathfind,
        "A*": astar_pathfind,
        "DFS": dfs_pathfind,
    }
    return algorithms.get(algorithm_name, bfs_pathfind)
