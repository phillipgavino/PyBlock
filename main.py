from block_placement import *
from stl_voxel_layer_converter import *
from gcodegenerator import *
from PyBlockGUI import *

if __name__ == "__main__":
    # Load STL file and extract voxel layer data
    layer_data = stl_to_voxel_layer_data("stl/3DBenchy.stl")

    centers_layers = []
    info_lst = []

    # Process each layer
    for z, data in enumerate(layer_data):
        # print_grid(data)
        # Optimize block placement using MCTS and extract data
        grid = find_best_combination_with_mcts(read_grid_from_data(data))
        centers = get_block_centers(grid, z)
        info = extract_final_block_info(grid)

        # Store results for all layers
        centers_layers.append(centers)
        info_lst.append(info)

        fig, ax = plt.subplots(figsize=(8, 8))
        draw_grid(grid, ax)
       
    
    # Flatten the results
    centers_flat = [center for layer in centers_layers for center in layer]
    info_flat = [info for layer in info_lst for info in layer]

    print(info_flat)
    print(centers_flat)
    plt.show()

    # Generate G-code and GUI instructions
    # gcode("3DBenchy_gcode.gcode", centers_flat)
    # pyblock_instuction_GUI(info_flat)








        
