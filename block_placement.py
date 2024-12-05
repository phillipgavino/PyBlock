import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
import random
import math

random.seed(1)


# Function to read the grid from a text file
def read_grid_from_data(layer_data):
    grids = []
    for data in layer_data:
        ref_data = np.flip(np.array(data), axis=0)
        grids.append(ref_data)
    return grids

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

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

class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state  # The grid and current block ID
        self.parent = parent
        self.action = action
        self.children = []
        self.visits = 0
        self.value = 0

    def is_fully_expanded(self):
        return len(self.children) == len(self.get_legal_actions())
    
    def get_legal_actions(self):
        grid, block_id = self.state
        rows, cols = len(grid), len(grid[0])

        # Define block sizes in descending priority
        prioritized_blocks = [
            ((2, 4), 8),  # Block size 2x4
            ((2, 3), 8),  # Block size 2x3
            ((2, 2), 8)   # Block size 2x2
        ]

        # prioritized_blocks = [
        # ((2, 4), 8),  # Block size 2x4
        # ((2, 2), 8)   # Block size 2x2
        # ]

        valid_actions = []

        # Iterate over each block size in priority order
        for block, _ in prioritized_blocks:
            for orientation in [(block[0], block[1]), (block[1], block[0])]:  # Horizontal and vertical
                for i in range(rows - orientation[0] + 1):
                    for j in range(cols - orientation[1] + 1):
                        # Check if the block can fit at this position
                        can_place = True
                        for x in range(orientation[0]):
                            for y in range(orientation[1]):
                                if grid[i + x][j + y] != 1:  # Check if the cell is not empty
                                    can_place = False
                                    break
                            if not can_place:
                                break
                        if can_place:
                            # Add valid placement action (top-left corner and block details)
                            valid_actions.append((i, j, orientation, block))

        # Return all valid actions
        return valid_actions

    def add_child(self, action):
        new_state = self.perform_action(self.state, action)
        child = Node(new_state, parent=self, action=action)
        self.children.append(child)
        return child

    def perform_action(self, state, action):
        grid, block_id = state
        i, j, (rows, cols), block = action

        # Create a new grid to reflect the updated state
        new_grid = [row[:] for row in grid]  # Deep copy of the grid

        # Apply the block to the new grid
        for x in range(rows):
            for y in range(cols):
                new_grid[i + x][j + y] = block_id  # Mark the cells with the block ID

        # print(f"Placed block {block} at ({i}, {j}) with orientation ({rows}x{cols}).")
        return new_grid, block_id + 1


def mcts(grid, iterations=1000):
    root = Node((grid, 2))
    best_grid = grid
    max_coverage = 0

    for _ in range(iterations):
        node = root
        # Selection: Traverse tree to find the best leaf node
        while node.is_fully_expanded() and node.children:
            node = select_best_child(node)

        # Expansion: Expand the leaf node if it is not fully expanded
        if not node.is_fully_expanded():
            legal_actions = node.get_legal_actions()
            untried_actions = [action for action in legal_actions if action not in [child.action for child in node.children]]
            if untried_actions:
                action = random.choice(untried_actions)
                node = node.add_child(action)

        # Simulation: Run a random simulation from the current state
        coverage, simulated_grid = simulate(node.state)
        if coverage > max_coverage:
            max_coverage = coverage
            best_grid = simulated_grid

        # Backpropagation: Update values up the tree
        backpropagate(node, coverage)

    return best_grid


def select_best_child(node, exploration_weight=1.0):
    def ucb_score(child):
        exploitation = child.value / (child.visits + 1e-6)
        exploration = math.sqrt(math.log(node.visits + 1) / (child.visits + 1e-6))
        return exploitation + exploration_weight * exploration

    return max(node.children, key=ucb_score)


def simulate(state):
    grid, block_id = state
    current_grid = [row[:] for row in grid]
    coverage = 0

    # Simulate full block placement with prioritized blocks
    prioritized_blocks = [
        ((2, 4), 8),  # Block size 2x4
        ((2, 3), 8),  # Block size 2x3
        ((2, 2), 8)   # Block size 2x2
    ]

    # prioritized_blocks = [
    #     ((2, 4), 8),  # Block size 2x4
    #     ((2, 2), 8)   # Block size 2x2
    # ]

    while True:
        legal_actions = []
        for block, _ in prioritized_blocks:
            legal_actions = Node((current_grid, block_id)).get_legal_actions()
            if legal_actions:
                break

        if not legal_actions:
            break

        # Select the first valid action for the largest block
        action = legal_actions[0]
        i, j, (rows, cols), _ = action
        for x in range(rows):
            for y in range(cols):
                current_grid[i + x][j + y] = block_id
        block_id += 1
        coverage += rows * cols

    return coverage, current_grid


def backpropagate(node, result):
    while node:
        node.visits += 1
        node.value += result
        node = node.parent


# Visualization and grid solving
def find_best_combination_with_mcts(grid):
    print("Running MCTS...")
    best_grid = mcts(grid, iterations=1000)  # Increase iterations as needed
    return best_grid


def get_block_centers(grid, z):
    block_positions = {}

    # Collect block boundaries
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            block_id = grid[i][j]
            if block_id > 1:  # Only consider blocks
                if block_id not in block_positions:
                    block_positions[block_id] = [i, j, i, j]  # top, left, bottom, right
                else:
                    block_positions[block_id][2] = max(block_positions[block_id][2], i)  # Update bottom
                    block_positions[block_id][3] = max(block_positions[block_id][3], j)  # Update right

    # Calculate block centers
    centers = []
    for block_id, (top, left, bottom, right) in block_positions.items():
        height = bottom - top + 1
        width = right - left + 1
        
        if (height == 2 and width == 3) or (height == 3 and width == 2):  # Bottom 2x2 portion for 2x3 block
            y = bottom - 0.5
            x = right - 0.5
        else:  # Default: Center of the whole block
            y = (top + bottom) / 2
            x = (left + right) / 2
        
        centers.append([x, y, z])

    return centers

def extract_final_block_info(grid):
    block_positions = {}

    # Collect block boundaries
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            block_id = grid[i][j]
            if block_id > 1:  # Only consider placed blocks
                if block_id not in block_positions:
                    block_positions[block_id] = [i, j, i, j]
                else:
                    block_positions[block_id][2] = max(block_positions[block_id][2], i)
                    block_positions[block_id][3] = max(block_positions[block_id][3], j)

    # Generate block information
    block_info = []
    for block_id, (top, left, bottom, right) in block_positions.items():
        height = bottom - top + 1
        width = right - left + 1

        match (height, width):
            case (2, 2):
                block_info.append([0])
            case (2, 3):
                block_info.append([1, 0])
            case (2, 4):
                block_info.append([2, 0])
            case (3, 2):
                block_info.append([1, 1])
            case (4, 2):
                block_info.append([2, 1])
    return block_info