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
 
G1 X34.5 Y224 Z46.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z198.89999999999998 ;raise block up to travel height
G1 X98.0 Y122.40000000000002 ;go to block placement point
G1 Z168.89999999999998 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z198.89999999999998 ;raise empty gripper up to travel height
 
G1 X34.5 Y224 Z46.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z198.89999999999998 ;raise block up to travel height
G1 X148.8 Y173.20000000000002 ;go to block placement point
G1 Z168.89999999999998 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z198.89999999999998 ;raise empty gripper up to travel height
 
G1 X34.5 Y224 ; finish by going back to block pickup corner but stay at final height
