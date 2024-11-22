from block_placement import *
from stl_voxel_layer_converter import *

if __name__ == "__main__":

    layer_data = stl_to_voxel_layer_data("Simple_Model_House.stl")
    
    
    for data in layer_data:
        grid = find_best_combination(read_grid_from_data(data))
        centers = get_block_centers(grid)

        