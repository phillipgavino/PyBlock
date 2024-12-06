# PyBlock: Optimized Block Building Robot

## Objective
Develop a program that processes STL models and produces gcode for a modified 3D printer to construct the model using building blocks.

Essentially, create a LEGO-styled slicer and printer!

## Requirements

* Voxelize an arbitrary STL model
* Find solution to build it from given block shapes
* Generate valid gcode to place each block in order
* Modify 3D printer for real world test

## Packages

For this project, we used the following packages:

* open3D
* PyQT6
* NumPy
* matplotlib

To install these packages you can use the pip install method for each.
```
pip install open3d
pip install PyQt6
pip install numpy
pip install matplotlib
```
However, we found that numpy must be downgraded to version 1.24.0 to work with open3d.
```
pip install --upgrade numpy==1.24.0
```

---

## STL to Voxelized Grids to Layer Data

```python
layer_data = stl_to_voxel_layer_data(file_name, adjustment_factor = 1)
```
takes two arguments: the STL model name and a scale adjustment factor (defaulted to a value of 1). This function utilizes open3D to process the STL model, scales the mesh to fit our printer’s build volume, turns it into a voxel grid, and translates that voxel grid to a list of lists of lists with ones and zeros. To avoid issues with overhangs in the model, the layer data is processed to add ones below any other ones in other layers. This binary list data is the layer information needed for the next function. 

An adjustment factor of less than 1 can be added to scale the model down in the case that the current size requires too many blocks.

We ran into an issue where all of the models we built were too tall. We found that this code needed to be adjusted to double the height in build volume and later have half of the layers removed to the appropriate size of the model. This is due to the fact that our blocks are two studs tall.

### Important Features of This Code

We first read the STL model and set it to a variable name.
```python
mesh = o3d.io.read_triangle_mesh(file_path)
```
With this mesh it is very important for us to scale it up or down to fit our build volume appropriately. We can find the bounding box, take the minimum and maximum coordinate values of the bounding box and take the difference to get the size of the bounding box in all axis directions.
```python
bounding_box = mesh.get_axis_aligned_bounding_box()
bounding_box_min = np.array(bounding_box.get_min_bound())
bounding_box_max = np.array(bounding_box.get_max_bound())
bounding_box_dimensions = bounding_box_max - bounding_box_min
```
We can define our target dimensions of our mesh and divide it by our bounding box dimensions. This will give us a 3x1 array of needed scale factors that will make each dimension meet our target dimension. Since we don’t want to change the aspect ratio of the model, we must take the minimum of the scale factors and apply that to the entire mesh. Our build volume is 18 studs wide, 13 studs deep, and 14 studs tall. We also multiply the scale factor by our adjustment factor to further adjust the model to be preferably sized by the user.
```python
target_dimensions = np.array([18, 13, 14])
scale_factors = target_dimensions / bounding_box_dimensions
uniform_scale_factor = min(scale_factors) * adjustment_factor
mesh.scale(uniform_scale_factor, center= mesh.get_center())
```
We now can turn our triangle mesh object into a voxel grid object.
```python
 voxel_grid = o3d.geometry.VoxelGrid.create_from_triangle_mesh(mesh, voxel_size=1)
```
We have code that will center our model appropriately to the center of the build area, which we will not be getting into here.

From the voxel grid we can get the voxel information for all of the voxels and extract the coordinate data. Initializing an empty list of lists of lists of zeros in the shape of 18x13x14, we can iterate through each coordinate of the voxels and set the corresponding position in the list of lists of lists to 1. 
```python
for coordinate in translated_voxel_coordinates:
        x_coor = int(coordinate[0])
        y_coor = int(coordinate[1])
        z_coor = int(coordinate[2])
        layer_data[z_coor][y_coor][x_coor] = 1
```
This creates layer info in python list form that shows where all of the voxels exist. Voxel grids are hollow so we must fill in the inside to be dense. We also want to add 1’s below any 1’s that are overhanging. We can iterate through all positions in the layer data and check to see if there is a 1 somewhere above that point and if so set it to 1 as well.
```python
for z_coor in range(len(layer_data)):
            for y_coor in range(len(layer_data[0])):
                for x_coor in range(len(layer_data[0][0])):
                    if not layer_data[z_coor][y_coor][x_coor]:
                        if sum([ layer_data[z][y_coor][x_coor] for z in range(z_coor,len(layer_data)) ]):
                            layer_data[z_coor][y_coor][x_coor] = 1
```
With this the layer data is ready to be sent to the code that finds the best block placements.

Note: When working with 3D objects in open3d such as triangle meshes and voxel grids it is helpful to visualize these objects. We can use open3d’s draw_geometries function under their visualization module.
```python
o3d.visualization.draw_geometries([mesh], width, height)
o3d.visualization.draw_geometries([voxel_grid], width, height)
```

---

## Block Placing Algorithm Overview
This script provides a framework for solving grid-based block placement problems using **Monte Carlo Tree Search (MCTS)**. It includes functionality for grid visualization, simulation, and extraction of results, making it suitable for optimizing block placements in a 2D grid.

---

### Key Features
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

### Functions and Classes

#### 1. Grid Operations
- **`read_grid_from_data(layer_data)`**
  - Reads and flips grid data for processing.
- **`print_grid(grid)`**
  - Prints a formatted grid to the console.

#### 2. Visualization
- **`draw_grid(grid, ax)`**
  - Renders the grid with custom colors and block IDs.
- **`draw_block_borders(ax, grid)`**
  - Adds borders around blocks with unique IDs.

#### 3. Core Algorithm
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

#### 4. Utility Functions
- **`find_best_combination_with_mcts(grid)`**
  - Runs the MCTS algorithm and returns the best grid configuration.
- **`get_block_centers(grid, z)`**
  - Calculates the 3D centers of blocks for visualization or analysis.
- **`extract_final_block_info(grid)`**
  - Extracts metadata about block placements (e.g., size and orientation).

---

### Usage

#### Example Workflow
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
<<<<<<< HEAD
=======
>>>>>>> 083462fe370af443a6b49001a7fe49ba370e3fd9
---

## Gcode Generation
Gcode is generated by a function called "gcode()" which is contained in the file "gcodegenerator.py" This function generates valid gcode to place all the blocks in the correct locations corresponding to the solution found by the monte carlo algorithm. It filters out common errors, converts to the appropriate coordinate system, and generates a functional .gcode file ready for printing.


### Inputs
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

### Processing:
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
### Outputs:
The gcode() function does not return anything. When it is run, the final .gcode file will be saved in the same directory as the main python script unless an invalid input was detected, in which case no file will be created and an error message will print. This file can directly be copied to an sd card and run on the physical printer as if it were any other normal 3d printing file.

---

## User Interface

For our user interface, we used PyQT6, an object-oriented user interface package.

### Creating Windows
To create a window, you create a class object with QMainWindow and QWidget for additional windows.
```python
class MyMainWindow(QMainWindow):
```
or
```python
class AnotherWindow(QWidget):
```
All structure and widgets within the window are set with the __init__ function definition.

A particular function that these windows must run to start the window is 
```python
super().__init__()
```

### Layouts

What is not as intuitive is how the formatting layouts work. For example, we want our main window to have multiple images lined horizontally with each other at the top of the window, a progress bar in the middle of the window, and buttons at the very bottom. To set the layouts we must set an overall page layout to be a “vertical box layout.” This means widgets or sub layouts added to a vertical box layout will be add in a descending order from top to bottom. We then want to add multiple “horizontal box layouts” to the overall page layout, as for the images, progress bar and brick counter, and the two buttons will all be side by side.
```python
page_layout = QVBoxLayout()
brick_layout = QHBoxLayout()
progress_layout = QHBoxLayout()
button_layout = QHBoxLayout()
            
page_layout.addLayout(brick_layout)
page_layout.addLayout(progress_layout)
page_layout.addLayout(button_layout)
```

### QLabels and Images

A very common widget is the QLabel so that you can add text to your GUI. The method to produce QLabels is straightforward, however adding images is not. Adding an image is done through the QLabel approach except instead of using text as an input you add what PyQT6 calls a pixmap. 
```python
self.image = QLabel()
pixmap = QPixmap(image_file_path)
scaled_pixmap = pixmap.scaled(width, height)
self.image.setPixmap(scaled_pixmap)
```
Creating labels with the self object allows them to be updated easier as the GUI is being used.

### Buttons

Buttons are another useful widget to make your GUI interactive. Once you define your button as seen below, you mush connect it to a function that you define outside of your __init__ function. That function you create will be the instructions for what you want the button to do to the GUI.
```python
next_button = QPushButton('Click Me')
next_button.clicked.connect(self.button_was_clicked)
```

These are only some of the more important features of PyQT6 and other widgets are easy to understand and the PyQT6 documentation is super helpful to understand all of their features.

>>>>>>> 24dea2b607f5b5832025eef6dcc1fb4561de44ca
