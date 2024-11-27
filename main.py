from block_placement import *
from stl_voxel_layer_converter import *

if __name__ == "__main__":

    layer_data = stl_to_voxel_layer_data("3DBenchy.stl")

    # print(len(layer_data))
    
    for data in layer_data:
        fig, ax = plt.subplots(figsize=(8, 8))

        grid = find_best_combination_with_mcts(read_grid_from_data(data))
        draw_grid(grid, ax)
        plt.show()

        centers = get_block_centers(grid)
        info = extract_final_block_info(grid)

        
