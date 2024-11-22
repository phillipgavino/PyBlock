import open3d as o3d
import numpy as np
from os import path

def stl_to_voxel_layer_data(file_name):

    # Get the directory of the current script
    script_dir = path.dirname(path.abspath(__file__))

    # Construct the full path to the file
    file_path = path.join(script_dir, file_name)

    # Reading stl model and visualizing it
    mesh = o3d.io.read_triangle_mesh(file_path)

    # Getting the bounding box that aligns with the axes (x,y,z)
    bounding_box = mesh.get_axis_aligned_bounding_box()

    # Finding the coordinates (3x1 arrays) of the corners that represent 
    # the minimum extent and maximum extent
    bounding_box_min = np.array(bounding_box.get_min_bound())
    bounding_box_max = np.array(bounding_box.get_max_bound())

    # By taking the difference of the max and min coordinates, we can 
    # find the bounding box dimensions
    bounding_box_dimensions = bounding_box_max - bounding_box_min

    # We want the model to fit inside the build volume, which has a 
    # volume of 18x18x7 (17x17x6 in terms of indexes)
    x_extent = 18
    y_extent = 18
    z_extent = 7
    # subtracting one since it will scale such that it will be from 0 to 
    # the target dimension (if we want z to go from 0 to 6 then
    # we need to scale the models height to 6 units tall)
    target_dimensions = np.array([x_extent-1, y_extent-1, z_extent-1])

    # By dividing our target dimensions by the current bounding box 
    # dimensions, we find scale factors that would have to be apply 
    # to each axis to meet the target dimensions
    scale_factors = target_dimensions / bounding_box_dimensions

    # Taking the minimum value of these scale factors, we get the 
    # scale factor necessary to scale the mesh uniformally to either
    # be 18 units wide in the x direction, 18 units wide in the y 
    # direction, or 7 units tall in the z direction
    uniform_scale_factor = min(scale_factors)
    mesh.scale(uniform_scale_factor, center= mesh.get_center())

    # with our mesh scaled to fit in 18x18x7 volume, we can verify 
    # our new dimensions
    mesh_min = np.array(mesh.get_min_bound())
    mesh_max = np.array(mesh.get_max_bound())
    fitted_dimensions = mesh_max - mesh_min
    width, depth, height = fitted_dimensions
    txt = 'The fitted dimensions are: Width: {x:.2f} Depth: {y:.2f} Height: {z:.2f}'
    print(txt.format(x=width, y=depth, z=height))

    # creating voxel grid from our fitted mesh
    voxel_grid = o3d.geometry.VoxelGrid.create_from_triangle_mesh(mesh, voxel_size=1)
    # o3d.visualization.draw_geometries([voxel_grid], width=1500, height=1500)

    # finding total number of voxels in voxel grid
    total_voxels = len(voxel_grid.get_voxels())

    # creating a list of all voxel coordinates
    voxel_coordinates = []
    for i in range(total_voxels):
        # appending the i'th grid index (coordinate) to voxel coordinates
        voxel_coordinates.append(list(voxel_grid.get_voxels()[i].grid_index))

    # Voxel indexes (what I am calling voxel_coordinates) are 
    # always pushed to [0,0,0] corner. We need to push these 
    # coordinates to have the voxels centered about the buildplate
    # and start at 0 in the z direction. So we only need to move the
    # x and y values of each voxel.
    voxel_grid_center = np.array([fitted_dimensions[0]/2, fitted_dimensions[1]/2, 0])
    build_plate_center = np.array([x_extent/2, y_extent/2, 0])
    # a translation of 4.8 blocks is realistically 4 blocks over so I use floor
    translation_to_center = np.floor(build_plate_center - voxel_grid_center)
    translated_voxel_coordinates = [list(coor + translation_to_center) for coor in voxel_coordinates]

    # creating a 18x18x7 grid list of zeros
    layer_data = [[[0 for x in range(x_extent)] for y in range(y_extent)] for z in range(z_extent)]

    # for each coordinate in the translated voxel coordinates
    # set the layer data coordinate to 1
    for coordinate in translated_voxel_coordinates:
        x_coor = int(coordinate[0])
        y_coor = int(coordinate[1])
        z_coor = int(coordinate[2])
        layer_data[z_coor][y_coor][x_coor] = 1

    def make_dense(layer_data):

        for z_coor in range(len(layer_data)):
            for x_coor in range(len(layer_data[0])):
                for y_coor in range(len(layer_data[0][0])):
                    if not layer_data[z_coor][y_coor][x_coor]:
                        if sum([ layer_data[z][y_coor][x_coor] for z in range(0,z_coor) ]) and sum([ layer_data[z][y_coor][x_coor] for z in range(z_coor,len(layer_data)) ]):
                            layer_data[z_coor][y_coor][x_coor] = 1
        
        return layer_data
    
    layer_data = make_dense(layer_data)

    return layer_data

# layer_data = stl_to_voxel_layer_data('3DBenchy.stl')



