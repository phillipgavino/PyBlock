from block_placement import *
from stl_voxel_layer_converter import *

if __name__ == "__main__":

    layer_data = stl_to_voxel_layer_data("stl/Simple_Model_House.stl")

    # print(len(layer_data))
    
    for z, data in enumerate(layer_data):
        fig, ax = plt.subplots(figsize=(8, 8))

        grid = find_best_combination_with_mcts(read_grid_from_data(data))

        centers = get_block_centers(grid, z)
        info = extract_final_block_info(grid)

        print(centers)
        print(info)

        draw_grid(grid, ax)
        plt.show()




        
