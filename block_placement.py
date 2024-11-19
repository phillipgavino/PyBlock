import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.colors import ListedColormap

# Grid dimensions
grid_rows = 18
grid_cols = 18

# Define blocks with sizes prioritized from large to small, and their respective limits
blocks = [
    ((4, 8), 3),
    ((4, 8), 3),
    ((4, 4), 3)
]

# Function to read the grid from a text file
def read_grid_from_file(filename):
    with open(filename) as f:
        grid0 = [list(map(int, line.strip().split(','))) for line in f]
    return grid0

# Function to rotate block dimensions (if required)
def rotate_block(block_size):
    rows, cols = block_size
    return (cols, rows)

def can_place_block(grid, top_left, block_size, rotated=False):
    rows, cols = block_size
    if rotated:
        rows, cols = rotate_block((rows, cols))
    
    i, j = top_left
    if i + rows > grid_rows or j + cols > grid_cols:
        return False
    return all(grid[i + x][j + y] == 1 for x in range(rows) for y in range(cols))

def place_block(grid, top_left, block_size, block_id, rotated=False):
    rows, cols = block_size
    if rotated:
        rows, cols = rotate_block((rows, cols))

    i, j = top_left
    for x in range(rows):
        for y in range(cols):
            grid[i + x][j + y] = block_id

def draw_grid(grid, ax, current_block=None):
    ax.clear()
    max_id = np.max(grid)

    # Create a custom colormap
    colors = ['white', 'lightgray'] + [plt.cm.tab20(i) for i in range(2, max_id + 2)]
    cmap = ListedColormap(colors[:max_id + 1])

    # Plot the grid with the custom colormap
    ax.imshow(grid, cmap=cmap, origin='upper', interpolation='none')
    draw_block_borders(ax, grid)
    ax.set_xticks(range(len(grid[0]) + 1))
    ax.set_yticks(range(len(grid) + 1))
    ax.grid(visible=False)

    # Add block IDs to the cells
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                ax.text(j, i, f'{grid[i][j]}', ha='center', va='center', color='black', fontsize=12, fontweight='bold')

    # Show the current block geometry
    if current_block:
        ax.set_title(f'Placing Block ID: {current_block}', fontsize=16)

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


def generate_grid(grid0):
    block_id = 2  # Start with 2 since 1s are used in the initial file
    coordinates = [(i, j) for i in range(grid_rows) for j in range(grid_cols)]
    random.shuffle(coordinates)  # Randomize placement order once

    fig, ax = plt.subplots(figsize=(8, 8))
    plt.ion()  # Turn on interactive mode

    for block_size, limit in blocks:
        count = 0
        for i, j in coordinates:
            if count >= limit:
                break

            if grid0[i][j] == 1:
                # Try placing the block in both orientations
                if can_place_block(grid0, (i, j), block_size):
                    place_block(grid0, (i, j), block_size, block_id)
                    draw_grid(grid0, ax, current_block=block_id)
                    plt.pause(1)  # Pause to show the placement
                    block_id += 1
                    count += 1
                elif can_place_block(grid0, (i, j), block_size, rotated=True):
                    place_block(grid0, (i, j), block_size, block_id, rotated=True)
                    draw_grid(grid0, ax, current_block=block_id)
                    plt.pause(1)  # Pause to show the placement
                    block_id += 1
                    count += 1
    plt.ioff()  # Turn off interactive mode
    plt.show()  # Keep the final visualization open
    return grid0

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
        if (height == 2 and width == 3) or (height == 3 and width == 2):
            # Center of the left 2x2 portion
            center_row = (top + top + 1) / 2
            center_col = (left + left + 1) / 2
        else:
            # Default: Center of the whole block
            center_row = (top + bottom) / 2
            center_col = (left + right) / 2
        
        centers.append((center_col, center_row))
    
    return centers


if __name__ == "__main__":
    grid = generate_grid(read_grid_from_file("grid_input.txt"))

    centers = get_block_centers(grid)

    print(centers)

