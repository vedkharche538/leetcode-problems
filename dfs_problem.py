### Array and out of which the connection is been made and we will iterate over each node where the next connection nodes will be in stack 
# ### since dfs uses stack as a main to iterate over all the nodes.
# import numpy as np

maze = [
  [0, 0, 1, 0],
  [1, 0, 1, 0],
  [0, 0, 0, 0],
  [0, 1, 1, 0]
]

def hasPath(maze, start, destination):
    if not maze or not maze[0]:
        return False
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [start]
    visited = set()
    visited.add(start)

    while stack:
        current = stack.pop()
        if current == destination:
            return True ## we found the destination that we were looking for
        
        row, col = current
        for dr, dc in directions:
            new_row = row + dr
            new_col =  col + dc

            # now we have updated the position and now i wanted to see the new position is valid or not?
            if (0<=new_row<len(maze)) and (0<=new_col<len(maze[0])) and maze[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                stack.append((new_row, new_col))
                visited.add((new_row, new_col))
    return False

# result = hasPath(maze, (0,0), (3,3))
# print(result)
area = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
def max_are_of_island(grid):
    if not grid and not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    max_area = 0

    def dfs(r, c):
        if r <0 or r >= rows or c <0 or c >= cols or grid[r][c] == '0':
            return 0
        grid[r][c] = '0'

        area = 1 + dfs(r-1,c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
        return area
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                max_area = max(max_area, dfs(r, c))
    return max_area


max_area = max_are_of_island(area)
print(max_area)




