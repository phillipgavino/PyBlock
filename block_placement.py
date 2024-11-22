import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.colors import ListedColormap
import copy

# Define blocks with sizes prioritized from large to small, and their respective limits
blocks = [
    ((4, 8), 1),
    ((4, 6), 2),
    ((4, 4), 3)
]

# Function to read the grid from a text file
def read_grid_from_data(layer_data):
    grids = []
    for data in layer_data:
        grids.append(data)
    return grids

# Function to rotate block dimensions (if required)
def rotate_block(block_size):
    rows, cols = block_size
    return (cols, rows)

def can_place_block(grid, top_left, block_size, rotated=False):
    rows, cols = block_size
    if rotated:
        rows, cols = rotate_block((rows, cols))
    
    i, j = top_left
    # Check if block fits within the grid boundaries
    if i + rows > len(grid) or j + cols > len(grid[0]):
        # print(f"Block {block_size} (rotated={rotated}) does not fit at {top_left}")
        return False
    
    # Check if all cells under the block are `1`
    valid = all(grid[i + x][j + y] == 1 for x in range(rows) for y in range(cols))
    # if not valid:
    #     print(f"Block {block_size} (rotated={rotated}) cannot be placed at {top_left}")
    return valid


def place_block(grid, top_left, block_size, block_id, rotated=False):
    rows, cols = block_size
    if rotated:
        rows, cols = rotate_block((rows, cols))

    i, j = top_left
    for x in range(rows):
        for y in range(cols):
            grid[i + x][j + y] = block_id


def draw_grid(grid, ax):
    ax.clear()

    # Ensure grid is a NumPy array with integer values
    grid = np.array(grid, dtype=int)

    # Compute the maximum block ID safely
    max_id = np.max(grid) if np.any(grid) else 0

    # Create a custom colormap
    colors = ['white', 'lightgray'] + [plt.cm.tab20(i % 20) for i in range(2, max_id + 2)]
    cmap = ListedColormap(colors[:max_id + 1])

    # Plot the grid with the custom colormap
    ax.imshow(grid, cmap=cmap, origin='upper', interpolation='none')

    # Set x and y limits to the dimensions of the grid
    ax.set_xlim(-0.5, len(grid[0]) - 0.5)
    ax.set_ylim(len(grid) - 0.5, -0.5)
    draw_block_borders(ax, grid)

    ax.set_xticks(range(len(grid[0]) + 1))
    ax.set_yticks(range(len(grid) + 1))
    ax.grid(visible=False)

    # Add block IDs to the cells
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                ax.text(j, i, f'{grid[i][j]}', ha='center', va='center', color='black', fontsize=12, fontweight='bold')


def draw_block_borders(ax, grid):
    block_positions = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            block_id = grid[i][j]
            if block_id > 1:  # Only consider block_ids greater than 1
                if block_id not in block_positions:
                    block_positions[block_id] = [i, j, i, j]
                else:
                    block_positions[block_id][2] = max(block_positions[block_id][2], i)
                    block_positions[block_id][3] = max(block_positions[block_id][3], j)

    for pos in block_positions.values():
        top, left, bottom, right = pos
        rect = plt.Rectangle((left - 0.5, top - 0.5), right - left + 1, bottom - top + 1,
                             edgecolor='black', linewidth=2, fill=False)
        ax.add_patch(rect)


def find_best_combination(grid):
    fig, ax = plt.subplots(figsize=(8, 8))
    # Cache to store the best grid configurations
    best_grid = None
    max_coverage = 0
    block_coverage = {tuple(size): 0 for size, _ in blocks}

    def backtrack(current_grid, block_id, current_coverage, coverage_tracker):
        nonlocal best_grid, max_coverage

        # Update the best grid if this arrangement has the most coverage
        if current_coverage > max_coverage:
            max_coverage = current_coverage
            best_grid = [row[:] for row in current_grid]

        # Try placing every block at every position
        for i in range(len(current_grid)):
            for j in range(len(current_grid[0])):
                if current_grid[i][j] != 1:
                    continue

                # Sort blocks in descending order of area (larger blocks first)
                for block_size, limit in sorted(blocks, key=lambda x: -(x[0][0] * x[0][1])):
                    if coverage_tracker[tuple(block_size)] >= limit:
                        continue  # Skip if the block limit is reached
                    
                    for rotated in [False, True]:
                        if can_place_block(current_grid, (i, j), block_size, rotated):
                            grid_copy = copy.deepcopy(current_grid)
                            rows, cols = block_size if not rotated else (block_size[1], block_size[0])
                            new_coverage = current_coverage + rows * cols
                            coverage_tracker[tuple(block_size)] += 1

                            place_block(current_grid, (i, j), block_size, block_id, rotated)

                            # Recurse
                            backtrack(current_grid, block_id + 1, new_coverage, coverage_tracker)

                            # Undo changes
                            current_grid = grid_copy
                            coverage_tracker[tuple(block_size)] -= 1

    # Initialize backtracking
    backtrack(grid, block_id=2, current_coverage=0, coverage_tracker=block_coverage)

    # If no blocks could be placed, best_grid will be None
    if best_grid is None:
        print("No blocks could be placed. Drawing the original grid.")
        best_grid = grid  # Use the original grid

    # Draw the resulting grid (original or with blocks placed)
    draw_grid(best_grid, ax)
    plt.show()
    return best_grid



def get_block_centers(grid):
    block_positions = {}
    
    # Collect block boundaries
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            block_id = grid[i][j]
            if block_id > 1:  # Only consider blocks
                if block_id not in block_positions:
                    block_positions[block_id] = [i, j, i, j]
                else:
                    block_positions[block_id][2] = max(block_positions[block_id][2], i)
                    block_positions[block_id][3] = max(block_positions[block_id][3], j)
    
    # Calculate block centers
    centers = []
    for block_id, (top, left, bottom, right) in block_positions.items():
        height = bottom - top + 1
        width = right - left + 1
        
        # Special cases
        if (height == 4 and width == 6) or (height == 6 and width == 4):
            # Center of the left 2x2 portion
            center_row = (top + top + 1) / 2
            center_col = (right + right + 1) / 2
        else:
            # Default: Center of the whole block
            center_row = (top + bottom) / 2
            center_col = (left + right) / 2
        
        centers.append((center_col, center_row))
    
    return centers

