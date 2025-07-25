from typing import List, Tuple, Set
# Escape the Maze
# This script finds a path through a maze represented as a grid.  
# 7/25/2025
# Define the maze as a grid of:
#   0 = open space
#   1 = wall
#   'E' = exit
Maze = List[List[object]]

# Four possible moves: down, right, up, left (feel free to reorder)
MOVES = [
    (1, 0, "DOWN"),
    (0, 1, "RIGHT"),
    (-1, 0, "UP"),
    (0, -1, "LEFT"),
]

def find_exit_path(maze: Maze, start: Tuple[int,int]) -> List[str]:
    """
    Returns a list of moves that takes the robot from `start` to the exit.
    If no path exists, returns an empty list.
    """
    rows, cols = len(maze), len(maze[0])
    visited: Set[Tuple[int,int]] = set()
    path: List[str] = []

    def dfs(r: int, c: int) -> bool:
        # Out of bounds or wall? Dead end.
        if not (0 <= r < rows and 0 <= c < cols):  
            return False
        if maze[r][c] == 1 or (r, c) in visited:
            return False
        # Found the exit!
        if maze[r][c] == 'E':
            return True

        visited.add((r, c))
        # Try each direction
        for dr, dc, move_name in MOVES:
            path.append(move_name)
            if dfs(r + dr, c + dc):
                return True
            # backtrack
            path.pop()

        return False

    # Kick off the search
    dfs(start[0], start[1])
    return path


if __name__ == "__main__":
    # Example maze
    maze = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 'E', 1],
        [1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1],
    ]
    start_position = (4, 1)  # anywhere inside the open area

    path = find_exit_path(maze, start_position)
    if path:
        print("Exit found! Move sequence:")
        print(" → ".join(path))
    else:
        print("No path to an exit exists from", start_position)
