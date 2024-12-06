## Overview
This script provides a framework for solving grid-based block placement problems using **Monte Carlo Tree Search (MCTS)**. It includes functionality for grid visualization, simulation, and extraction of results, making it suitable for optimizing block placements in a 2D grid.

---

## Key Features
1. **Grid Handling:**
   - Reading, printing, and visualizing grids with block placements.
   - Displays grids with block IDs and optional borders around blocks.

2. **MCTS Algorithm:**
   - Implements a tree-based search algorithm to find optimal block placements.
   - Includes selection, expansion, simulation, and backpropagation phases.

3. **Block Management:**
   - Prioritizes blocks of different sizes (e.g., 2x4, 2x3, 2x2).
   - Calculates block centers and generates placement metadata for analysis.

4. **Visualization:**
   - Renders grids with block placements using **Matplotlib**.
   - Highlights block IDs and borders to improve clarity.

---

## Functions and Classes

### 1. Grid Operations
- **`read_grid_from_data(layer_data)`**
  - Reads and flips grid data for processing.
- **`print_grid(grid)`**
  - Prints a formatted grid to the console.

### 2. Visualization
- **`draw_grid(grid, ax)`**
  - Renders the grid with custom colors and block IDs.
- **`draw_block_borders(ax, grid)`**
  - Adds borders around blocks with unique IDs.

### 3. Core Algorithm
- **`Node` Class**
  - Represents a state in the MCTS tree.
  - Supports actions, child management, and state transitions.
- **`mcts(grid, iterations=1000)`**
  - Performs Monte Carlo Tree Search to optimize block placements.
- **`select_best_child(node, exploration_weight=1.0)`**
  - Chooses the most promising child node based on a UCB score.
- **`simulate(state)`**
  - Simulates block placements to evaluate grid coverage.
- **`backpropagate(node, result)`**
  - Updates node values and visit counts during MCTS.

### 4. Utility Functions
- **`find_best_combination_with_mcts(grid)`**
  - Runs the MCTS algorithm and returns the best grid configuration.
- **`get_block_centers(grid, z)`**
  - Calculates the 3D centers of blocks for visualization or analysis.
- **`extract_final_block_info(grid)`**
  - Extracts metadata about block placements (e.g., size and orientation).

---

## Usage

### Example Workflow
1. **Input Grid Data:**
   Define the grid with initial block configurations:
   ```python
   initial_grid = [
       [1, 1, 1, 0],
       [1, 1, 1, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]
   ]
   ```

2. **Run MCTS:**
   Use the find_best_combination function to optimize placements:
   ```python
   optimized_grid = find_best_combination_with_mcts(intitial_grid)
   ```

3. **Visualize Results:**
  Display the optimized grid:
  ```python
  fig, ax = plt.subplots()
  draw_grid(optimized_grid, ax)
  plt.show()
  ```

4. **Extract Block Metadata:**
  Analyze final block placements:
  ```python
  block_info = extract_final_block_info(optimized_grid) 
  print(block_info)
  ```
>>>>>>> 083462fe370af443a6b49001a7fe49ba370e3fd9
