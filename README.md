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
---

# GCODE GENERATION
Gcode is generated by a function called "gcode()" which is contained in the file "gcodegenerator.py" This function generates valid gcode to place all the blocks in the correct locations corresponding to the solution found by the monte carlo algorithm. It filters out common errors, converts to the appropriate coordinate system, and generates a functional .gcode file ready for printing.


### INPUTS:
This function takes two inputs. The first is a filename, which can be any string. If it does not end in ".gcode" already, that will be added. The second input is the block placement points in the form of integers. The lower left peg is 0,0 and the first z axis layer is 0. The input coordinates (x,y,z) are in integer numbers of pegs relative to this zero. For example, the center point for a 2x2 block placed in the lower left corner would be (0.5, 0.5, 0). This is because the center of the block is halfway between its two pegs in both x and y. Note that for 2x2 and 2x4 blocks, the centerpoint is defined as their geometric center, regardless of orientation. For the odd 2x3 block, the centerpoint is offset to one side such that the point is centered between 4 studs. In the vertical case (3 long side along y), the point will be centered around the lower 4 studs (-y direction). In the horizontal case (3 long side along x), the point will be centered around the right side (+x direction). Z will always be an integer depending on the vertical layer. gcode() will accept these (x,y,z) points in the form of a list of lists, or a numpy array of numpy arrays. See an example of each below.


#### Example inputs:
```
#Example input for stacking six blocks on top of eachother in the front left corner:
p1 = np.array([0.5, 0.5, 0])
p2 = np.array([0.5, 0.5, 1])
p3 = np.array([0.5, 0.5, 2])
p4 = np.array([0.5, 0.5, 3])
p5 = np.array([0.5, 0.5, 4])
p6 = np.array([0.5, 0.5, 5])
pointstest = np.array([p1,p2,p3,p4,p5,p6])
gcode("test2.gcode", pointstest)
```
```
#Example input that uses lists of lists instead of numpy arrays:
p1 = [0.5, 0.5, 0]
p2 = [0.5, 0.5, 2]
p3 = [0.5, 0.5, 1]
pointstest = [p1, p2, p3]
gcode("test3.gcode", pointstest)
```

### PROCESSING:
The order of the block centerpoints does not matter. gcode() will always sort by the z coordinate in ascending order, so the lowest layers are placed first. gcode() will filter out a few invalid conditions from the input and prevend a .gcode file from being created, printing an error message instead.
Invalid geometry inputs include no blocks on the first layer, blocks misaligned with pegs, non integer z values, or an incorrectly structured input. These will all prevent a .gcode file from being written.

gcode() converts the centerpoints into the 3D printer’s coordinate system. This is in millimeters from the printer zero, where it homes against the limit switches. gcode() accounts for a fixed offset between the printer zero and block pickup point, located in the back left corner (-x, +y direction). Absolute coordinates in millimeters from printer zero are determined for each block placement by adding 0.5” increments in x/y from the pickup point to align with integer numbers of studs. The z axis has an offset applied to ensure the effector height is correct for the pickup point. Subsequent z coordinates are placed in increments of 1” (the block height) based on the integer number from the input z coordinate. A further z offset is applied during travel for extra clearance above previously placed blocks.

A gcode header is added to every file at the top which is the same every time. It sets some settings for the printer before movement begins. This default header is shown below. Note, the actual number values will depend on predetermined offsets.
```
M82 ;absolute extrusion mode
M201 X500.00 Y500.00 Z100.00 E5000.00 ;Setup machine max acceleration
M203 X500.00 Y500.00 Z10.00 E50.00 ;Setup machine max feedrate
M204 P500.00 R1000.00 T500.00 ;Setup Print/Retract/Travel acceleration
M205 X8.00 Y8.00 Z0.40 E5.00 ;Setup Jerk
M220 S100 ;Reset Feedrate
M221 S100 ;Reset Flowrate
M302 S0 ;Disable cold extrusion safety
G28 ;Home
G92 E0
G1 X0 Y0 Z46.5 F1000      ;raise z above zero point
G1 X34.5 Y224 Z46.5  ;go high above block pickup point
```
Then, a section of gcode is generated for each block location to pick it up, move it, and place it. An example section with comments is shown below. These comments appear in the final gcode file so that it is more human readable.
```
G1 X34.5 Y224 Z46.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z46.5 ;raise block up to travel height
G1 X98.0 Y122.4 ;go to block placement point
G1 Z16.5 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z46.5 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
```
### OUTPUTS:
The gcode() function does not return anything. When it is run, the final .gcode file will be saved in the same directory as the main python script unless an invalid input was detected, in which case no file will be created and an error message will print. This file can directly be copied to an sd card and run on the physical printer as if it were any other normal 3d printing file.

---
