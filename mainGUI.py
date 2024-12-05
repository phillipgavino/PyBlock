from PyBlockGUI import *
from stl_voxel_layer_converter import *

if __name__ == "__main__":

    # brick_data = [[0],[1,0],[2,1],[1,1],[0],[2,0]]
    # # brick_data = [[1,0],[2,1],[1,1],[2,0]]

    # pyblock_instuction_GUI(brick_data)

    layer_data = stl_to_voxel_layer_data('Armchair.stl')

    for layer in layer_data:
        for row in layer:
            print(row)