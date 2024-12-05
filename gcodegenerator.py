# Gcode Builder
import numpy as np

def gcode(filename, points):
    #filename is the name of the gcode file that will be output. must end in .gocode. example "benchy.gcode"
    # points is a numpy array of numpy arrays, or a list of lists in the same format: [[x,y,z],[x,y,z],[x,y,z]] corresponding to grab locations for each block in integer numbers of pegs from 0,0
    # origin (0,0) is the bottom left peg on the platform (near where printer zeroes itself.)
    
    if not filename.endswith(".gcode"): #add .gcode to the filename if it was omitted
        filename = filename + ".gcode"
        
    # sort the points, handles both numpy arrays and lists of lists
    if isinstance(points, list):
        sortedpoints = sorted(points, key = lambda val: val[2])  #sort the incoming points by z height
    elif isinstance(points, np.ndarray): 
        sortedpoints = points[points[:, 2].argsort()]  #sort the incoming points by z height
    else:
        print("\nTHIS INPUT IS INVALID. USE A LIST OF LISTS OR A NUMPY ARARY OF NUMPY ARRAYS\n[[x,y,z],[x,y,z],[x,y,z]]\n")
        return
    # print(sortedpoints)

    for p in sortedpoints:
        err1 = False
        err2 = False
        if not p[0]%1 == 0.5:
            err1 = True
        if not p[1]%1 == 0.5:
            err1 = True
        if not p[2]%1 == 0:
            err2 = True
        if err1:
            print("\nINVALID PLACEMENT POINT IN INPUT. X AND Y MUST END IN 0.5\n")
            return
        if err2:
            print("\nINVALID Z VALUE IN INPUT. MUST BE INTEGERS.\n")
            return
    
    if not sortedpoints[0][2] == 0:
        print("\nEMPTY FIRST LAYER. MUST HAVE AT LEAST ONE Z VALUE OF 0\n")
        return


    xOffset = 34.5   #mm offsets from point where printer zeroes against its limit switches to pickup point of the blocks
    yOffset = 224
    zOffset = 16.5 #height the effector should be when it grabs the block
    zTravel = 50 #extra z clearance to raise the block up when traveling around

    header = "M82 ;absolute extrusion mode\n"
    header = header + "M201 X500.00 Y500.00 Z100.00 E5000.00 ;Setup machine max acceleration\n"
    header = header + "M203 X500.00 Y500.00 Z100.00 E50.00 ;Setup machine max feedrate\n"
    header = header + "M204 P500.00 R1000.00 T500.00 ;Setup Print/Retract/Travel acceleration\n"
    header = header + "M205 X8.00 Y8.00 Z0.40 E5.00 ;Setup Jerk\n"
    header = header + "M220 S500 ;Reset Feedrate\n"
    header = header + "M221 S100 ;Reset Flowrate\n"
    header = header + "M302 S0 ;Disable cold extrusion safety\n"
    header = header + "G28 ;Home\n"
    header = header + "G92 E0\n"
    header = header + "G1 X0 Y0 Z"+str(zOffset+zTravel)+" F1000      ;raise z above zero point\n"
    header = header + "G1 X"+str(xOffset)+" Y"+str(yOffset)+" Z"+str(zOffset+zTravel)+"  ;go high above block pickup point"
    header = header + " \n" #empty line to separate header

    with open(filename, "w") as file:
        file.write(header)

        for p in sortedpoints:
            x = xOffset - 1.5*12.7 + (p[0]*12.7)
            y = yOffset - 14.5*12.7 + (p[1]*12.7)
            z = zOffset + (p[2]*25.4)
            block = " \n"
            block = block + "G1 X"+str(xOffset)+" Y"+str(yOffset) +" Z"+str(zOffset+zTravel)+" ;go high above block pickup point\n"
            block = block + "G1 Z"+str(zOffset)+" ; descend to block pickup point height\n"
            block = block + "G1 E4 ;lock in gripper\n"
            block = block + "G4 P500 ;pause\n"
            block = block + "G1 Z"+str(z + zTravel)+" ;raise block up to travel height\n"
            block = block + "G1 X"+str(x)+" Y"+str(y)+" ;go to block placement point\n"
            block = block + "G1 Z"+str(z)+" ;descend to block placement height\n"
            block = block + "G1 E0 ;release gripper\n"
            block = block + "G4 P500 ;pause\n"
            block = block + "G1 Z"+str(z + zTravel)+" ;raise empty gripper up to travel height\n"
            block = block + "G4 P5000; long pause before next block pickup\n"
            file.write(block)

        footer = " \n"
        footer = footer + "G1 X"+str(xOffset)+" Y"+str(yOffset)+" ; finish by going back to block pickup corner but stay at final height\n"
        file.write(footer)

# Example code for generating gcode that places 3 blocks in a file called "test1.gcode"
# p1 = np.array([0.5, 0.5, 0])
# p2 = np.array([4.5, 4.5, 0])
# p3 = np.array([0.5, 0.5, 1])
# pointstest = np.array([p1,p2,p3])
# gcode("test1.gcode", pointstest)

# Example for stacking six blocks on top of eachother in the front left corner
# p1 = np.array([0.5, 0.5, 0])
# p2 = np.array([0.5, 0.5, 1])
# p3 = np.array([0.5, 0.5, 2])
# p4 = np.array([0.5, 0.5, 3])
# p5 = np.array([0.5, 0.5, 4])
# p6 = np.array([0.5, 0.5, 5])
# pointstest = np.array([p1,p2,p3,p4,p5,p6])
# gcode("test2.gcode", pointstest)

#Example that uses lists of lists instead of numpy arrays
# p1 = [0.5, 0.5, 0]
# p2 = [0.5, 0.5, 2]
# p3 = [0.5, 0.5, 1]
# pointstest = [p1, p2, p3]
# gcode("test3.gcode", pointstest)
