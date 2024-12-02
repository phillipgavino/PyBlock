# Gcode Builder
import numpy as np

def gcode(filename, points):
    xOffset = 34.5   #mm offsets from point where printer zeroes against its limit switches to pickup point of the blocks
    yOffset = 224
    zOffset = 16.5 #height the effector should be when it grabs the block
    zTravel = 30 #extra z clearance to raise the block up when traveling around

    header = "M82 ;absolute extrusion mode\n"
    header = header + "M201 X500.00 Y500.00 Z100.00 E5000.00 ;Setup machine max acceleration\n"
    header = header + "M203 X500.00 Y500.00 Z10.00 E50.00 ;Setup machine max feedrate\n"
    header = header + "M204 P500.00 R1000.00 T500.00 ;Setup Print/Retract/Travel acceleration\n"
    header = header + "M205 X8.00 Y8.00 Z0.40 E5.00 ;Setup Jerk\n"
    header = header + "M220 S100 ;Reset Feedrate\n"
    header = header + "M221 S100 ;Reset Flowrate\n"
    header = header + "M302 S0 ;Disable cold extrusion safety\n"
    header = header + "G28 ;Home\n"
    header = header + "G92 E0\n"
    header = header + "G1 X0 Y0 Z"+str(zOffset+zTravel)+" F1000      ;raise z above zero point\n"
    header = header + "G1 X"+str(xOffset)+" Y"+str(yOffset)+" Z"+str(zOffset+zTravel)+"  ;go high above block pickup point"
    header = header + " \n" #empty line to separate header

    with open(filename, "w") as file:
        file.write(header)

        for p in points:
            # x = xOffset - 1*25.4 + (p[0]*25.4)
            # y = yOffset - 7.5*25.4 + (p[1]*25.4) #that extra offset acccounts for putting origin at bottom left corner, peg 0 0
            x = xOffset - 1.5*12.7 + (p[0]*12.7)
            y = yOffset - 14.5*12.7 + (p[0]*12.7)
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


#this line is for testin gpurposes only