# Shortest Path Visualizer (Python + Pygame)
A visualization tool to compare and analyze four major pathfinding algorithms:
- BFS (Breadth-First Search)
- DFS (Depth-First Search)
- Dijkstra’s Algorithm
- A* Search Algorithm

This project includes support for:
- Multiple intermediate waypoints
- Delay-based traversal cost
- Real-time visual exploration of grids
- Interactive Pygame interface

---

## Overview
This project demonstrates how different pathfinding algorithms explore a grid and compute paths under different conditions, including:
- Obstacles
- Weighted nodes
- Waypoints with custom traversal delays

The visualizer helps users understand algorithm behavior, efficiency trade-offs, and how delays influence weighted searches like Dijkstra and A*.

---

## Features
### Grid Interaction
- Click to place/remove obstacles  
- Set Start and End nodes  
- Add multiple waypoints  
- Assign delay values to waypoints  

### Algorithm Visualization
- BFS (unweighted shortest path)
- DFS (deep traversal)
- Dijkstra (weighted shortest path)
- A* (Manhattan heuristic, weighted)

### Delay Simulation
- Each waypoint can have a delay value
- Integrated into Dijkstra and A* cost calculations

### UI Controls
- Buttons to select algorithms
- Buttons to add waypoint, set delay, clear board, and run visualizations
- Animated traversal of algorithms

---
